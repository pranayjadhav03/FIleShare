from django.contrib import admin
from .models import SharedFile
from django.utils import timezone
import os

@admin.register(SharedFile)
class SharedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'expiry', 'is_expired')
    actions = ['delete_expired_files']

    @admin.action(description='Delete expired files')
    def delete_expired_files(self, request, queryset):
        expired_files = SharedFile.objects.filter(expiry__lt=timezone.now())
        deleted_count = 0

        for file in expired_files:
            if file.file:
                if os.path.isfile(file.file.path):
                    os.remove(file.file.path)
            file.delete()
            deleted_count += 1

        self.message_user(request, f"Deleted {deleted_count} expired file(s) successfully.")
