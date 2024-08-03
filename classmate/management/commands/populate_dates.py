from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from classmate.models import DateDim

class Command(BaseCommand):
    help = 'Populate DateDim model with dates from 2020 to 2100'

    def handle(self, *args, **kwargs):
        # Define start and end dates
        start_date = timezone.datetime(2020, 1, 1)  # Start from January 1, 2020
        end_date = timezone.datetime(2100, 12, 31)  # End at December 31, 2100

        current_date = start_date

        while current_date <= end_date:
            # Ensure the date is the Monday of the week
            week_commencing = current_date - timedelta(days=current_date.weekday())

            # Create DateDim object and save
            DateDim.objects.create(week_commencing=week_commencing)

            # Move to the next Monday (start of next week)
            current_date += timedelta(days=7)

        self.stdout.write(self.style.SUCCESS('DateDim populated successfully'))
