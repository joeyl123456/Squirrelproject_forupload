import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Sight


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        def convert_bool(str_):
            if str(str_) in ['TRUE', 'true', 'True']:
                str_ = True
            elif str(str_) in ['FALSE', 'false', 'False']:
                str_ = False
            else:
                str_ = None
            return str_

        for item in data:
            s = Sight(
                Longitude=item['X'],
                Latitude=item['Y'],
                Unique_Squirrel_Id=item['Unique Squirrel ID'],
                Shift=item['Shift'],
                Date=datetime.datetime.strptime(item['Date'], '%m%d%Y'),
                Age=item['Age'],
                Primary_Fur_Color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_Location=item['Specific Location'],
                Running=convert_bool(item['Running']),
                Chasing=convert_bool(item['Chasing']),
                Climbing=convert_bool(item['Climbing']),
                Eating=convert_bool(item['Eating']),
                Foraging=convert_bool(item['Foraging']),
                Other_Activities=item['Other Activities'],
                Kuks=convert_bool(item['Kuks']),
                Quaas=convert_bool(item['Quaas']),
                Moans=convert_bool(item['Moans']),
                Tail_Flags=convert_bool(item['Tail flags']),
                Tail_Twitches=convert_bool(item['Tail twitches']),
                Approaches=convert_bool(item['Approaches']),
                Indifferent=convert_bool(item['Indifferent']),
                Runs_From=convert_bool(item['Runs from']),
            )
            s.save()
