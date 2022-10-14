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
            count_added_sensor = 0
            df_sensors = df.drop_duplicates(subset=['libelle'], keep='last')
            for _, row in tqdm(df_sensors.iterrows(), total=df_sensors.shape[0], desc="Adding sensors"):
                _, created = Sensor.objects.get_or_create(
                    name=row["libelle"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                )
            if created:
                count_added_sensor += 1
            self.stdout.write(self.style.SUCCESS(
                f'{count_added_sensor} sensors added.'))

        if add_observation:
            Observation.objects.all().delete()
            sensor_dict = dict(Sensor.objects.all().values_list('name', 'id'))
            obs_to_create = []
            for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Adding observations"):
                obs_to_create.append(Observation(
                    sensor_id=sensor_dict[row["libelle"]],
                    record_time=row["Date et heure de comptage"],
                    record_number=row["comptage_5m"],
                ))

            Observation.objects.bulk_create(obs_to_create)
            self.stdout.write(self.style.SUCCESS(
                f'{len(obs_to_create)} observations added.'))
