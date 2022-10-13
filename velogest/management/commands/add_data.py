from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import pandas as pd
from tqdm import tqdm

from velogest.models import Sensor, Observation


class Command(BaseCommand):
    help = 'Add sensors and observations from csv file.'

    def add_arguments(self, parser):
        # Définition des options argparse
        parser.add_argument('--file', type=str, required=True)
        parser.add_argument('--add_sensor', action='store_true')
        parser.add_argument('--add_observation', action='store_true')

    def handle(self, *args, **options):
        # self.stdout.write('Command started')

        csv_filepath = options.get("file")
        add_sensor = options.get("add_sensor", False)
        add_observation = options.get("add_observation", False)

        if Path(csv_filepath).is_file():
            df = pd.read_csv(csv_filepath)
            df["Geo Point"].str.split(",", expand=True)
            df = df.join(df["Geo Point"].str.split(",", expand=True).rename(
                columns={0: "latitude", 1: "longitude"}))
            df[["latitude", "longitude"]] = df[[
                "latitude", "longitude"]].astype(float)
            df["comptage_5m"] = df["comptage_5m"].fillna(0).astype(int)
            # print(df.info())
        else:
            self.stdout.write(f"{csv_filepath} doesn't exist !")
            return

        if add_sensor:
            df_sensors = df.drop_duplicates(subset=['libelle'], keep='last')
            for _, row in tqdm(df_sensors.iterrows(), total=df_sensors.shape[0], desc="Adding sensors"):
                Sensor.objects.get_or_create(
                    name=row["libelle"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                )

        if add_observation:
            df_sample = df.sample(1000, random_state=123)
            for _, row in tqdm(df_sample.iterrows(), total=df_sample.shape[0], desc="Adding observations"):
                Observation.objects.get_or_create(
                    sensor=Sensor.objects.get(name=row["libelle"]),
                    record_time=row["Date et heure de comptage"],
                    record_number=row["comptage_5m"],
                )

        # Traitements
        # if something_wrong:
        #     raise CommandError("Something went wrong")
        # self.stdout.write(self.style.SUCCESS('Command ended'))
