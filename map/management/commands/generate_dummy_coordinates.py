import time
import random
from django.core.management.base import BaseCommand
from user.models import User
from map.models import Coordinates


# Cebu City center coordinates
BASE_LAT = 10.3157
BASE_LNG = 123.8854
# Spread radius (~2km in degrees)
SPREAD = 0.018


class Command(BaseCommand):
    help = 'Generate dummy GPS coordinates for all firefighters and trucks with tracker IDs'

    def add_arguments(self, parser):
        parser.add_argument(
            '--once',
            action='store_true',
            default=False,
            help='Generate one batch of coordinates and exit',
        )
        parser.add_argument(
            '--interval',
            type=int,
            default=0,
            help='Run continuously, generating coordinates every N seconds',
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
        once = options['once']
        interval = options['interval']
        base_lat = options['lat']
        base_lng = options['lng']
        spread = options['spread']

        # Get all trackable users
        users = User.objects.filter(
            role__in=[User.Role.FIREFIGHTER, User.Role.TRUCK],
            tracker_id__isnull=False,
        ).exclude(tracker_id='')

        if not users.exists():
            self.stdout.write(self.style.WARNING(
                'No firefighter or truck users with tracker_id found. '
                'Please assign tracker IDs to users first.'
            ))
            return

        self.stdout.write(self.style.SUCCESS(
            f'Found {users.count()} trackable users:'
        ))
        for user in users:
            self.stdout.write(f'  - {user.username} (role={user.role}, tracker_id={user.tracker_id})')

        # Track last known positions for smooth movement
        last_positions = {}

        if once or (not once and interval == 0):
            # Single batch mode
            count = self._generate_batch(users, base_lat, base_lng, spread, last_positions)
            self.stdout.write(self.style.SUCCESS(
                f'Generated {count} coordinate entries.'
            ))
        elif interval > 0:
            # Continuous mode
            self.stdout.write(self.style.SUCCESS(
                f'Running continuously every {interval} seconds. Press Ctrl+C to stop.'
            ))
            try:
                while True:
                    count = self._generate_batch(users, base_lat, base_lng, spread, last_positions)
                    self.stdout.write(f'[{time.strftime("%H:%M:%S")}] Generated {count} coordinates')
                    time.sleep(interval)
            except KeyboardInterrupt:
                self.stdout.write(self.style.SUCCESS('\nStopped.'))

    def _generate_batch(self, users, base_lat, base_lng, spread, last_positions):
        """Generate one batch of coordinates for all trackable users."""
        count = 0
        for user in users:
            tracker_id = user.tracker_id

            if tracker_id in last_positions:
                # Small random movement from last position
                last_lat, last_lng = last_positions[tracker_id]
                lat = last_lat + random.uniform(-0.002, 0.002)
                lng = last_lng + random.uniform(-0.002, 0.002)
            else:
                # Initial random position near base
                lat = base_lat + random.uniform(-spread, spread)
                lng = base_lng + random.uniform(-spread, spread)

            last_positions[tracker_id] = (lat, lng)

            Coordinates.objects.create(
                tracker_id=tracker_id,
                latitude=lat,
                longitude=lng,
            )
            count += 1

        return count
