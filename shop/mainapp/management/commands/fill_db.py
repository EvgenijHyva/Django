from django.core.management.base import BaseCommand
from django.core import serializers
from django.conf import settings
from django.db import IntegrityError

from mainapp import models
import json
import os
from pathlib import Path

class Command(BaseCommand):
    source = "fixtures"
    folder = ""

    def find_fixtures_folder(self, location):
        if self.source not in os.listdir(location):
            if location == settings.BASE_DIR:
                print(f"Folder <{self.source}> not found.\nCreated <{self.source}> in root.")
                os.mkdir(location / self.source)
                self.folder = location / self.source
                return
            self.find_fixtures_folder(location.parent)
        else:
            self.folder = location / self.source
            return

    def get_fixtures_files(self):
        location = Path(__file__).parent
        self.find_fixtures_folder(location)
        return os.listdir(self.folder)


    def load_from_json(self, file_name):
        with open(os.path.join(file_name), "r", encoding='utf-8') as file:
            return json.load(file)

    def find_model(self, name):
        model = models.__dict__.get(name)
        return model

    def write_data(self, model, data):
        for item in data:
            try:
                model.objects.create(**item["fields"])
            except IntegrityError:
                print("Already exists. Skipping")
            except ValueError as err:
                print(f"Error: {err}")


    def handle(self, *args, **options):
        files = self.get_fixtures_files()
        for file in files:
            data = self.load_from_json(self.folder / file)
            model_name = file[:file.find(".")].title()
            model = self.find_model(model_name)
            self.write_data(model, data)

        if not files:
            print("Nothing to load")