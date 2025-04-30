from django.core.management.base import BaseCommand
from core.models import SharedFile
from django.utils import timezone
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Deletes expired files from the database and disk.'

    def handle(self, *args, **options):
        expired_files = SharedFile.objects.filter(expiry__isnull=False, expiry__lt=timezone.now())
        count = expired_files.count()

        for shared_file in expired_files:
            # First delete the physical file
            if shared_file.file and os.path.isfile(shared_file.file.path):
                os.remove(shared_file.file.path)
                self.stdout.write(self.style.SUCCESS(f"Deleted file from disk: {shared_file.file.path}"))

            # Then delete the database record
            shared_file.delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} expired files'))
