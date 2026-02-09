import random
from django.core.management.base import BaseCommand
from user.models import Firestation

# Cebu City center and spread
BASE_LAT = 10.3157
BASE_LNG = 123.8854
SPREAD = 0.025  # ~2.5km radius


class Command(BaseCommand):
    help = 'Set random Cebu City coordinates for fire stations that do not have location data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            default=False,
            help='Overwrite coordinates for ALL fire stations, not just those missing them',
        )
        parser.add_argument(
            '--lat',
            type=float,
            default=BASE_LAT,
            help=f'Base latitude (default: {BASE_LAT})',
        )
        parser.add_argument(
            '--lng',
            type=float,
            default=BASE_LNG,
            help=f'Base longitude (default: {BASE_LNG})',
        )
        parser.add_argument(
            '--spread',
            type=float,
            default=SPREAD,
            help=f'Random spread radius in degrees (default: {SPREAD})',
        )

    def handle(self, *args, **options):
        overwrite_all = options['all']
        base_lat = options['lat']
        base_lng = options['lng']
        spread = options['spread']

        if overwrite_all:
            firestations = Firestation.objects.all()
        else:
            firestations = Firestation.objects.filter(
                latitude__isnull=True
            ) | Firestation.objects.filter(longitude__isnull=True)

        if not firestations.exists():
            self.stdout.write(self.style.WARNING(
                'No fire stations found that need coordinates. '
                'Use --all to overwrite existing coordinates.'
            ))
            return

        count = 0
        for fs in firestations:
            lat = base_lat + random.uniform(-spread, spread)
            lng = base_lng + random.uniform(-spread, spread)
            fs.latitude = lat
            fs.longitude = lng
            fs.save(update_fields=['latitude', 'longitude'])
            self.stdout.write(f'  {fs.name} (id={fs.id}): ({lat:.6f}, {lng:.6f})')
            count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Successfully set coordinates for {count} fire station(s).'
        ))
