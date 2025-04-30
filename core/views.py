from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404, HttpResponseForbidden
from .models import SharedFile
import uuid
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages 

def home(request):
    return render(request, 'core/home.html')

def view_file(request, file_uuid):
    file_obj = get_object_or_404(SharedFile, uuid=file_uuid)

    if file_obj.password:
        if request.method == 'POST':
            entered_password = request.POST.get('password')
            if entered_password == file_obj.password:
                messages.success(request, "Password correct! Download ready ✅")
                return render(request, 'core/view_file.html', {'file': file_obj, 'password_verified': True})
            else:
                messages.error(request, "Wrong password! Try again 🔒")
        return render(request, 'core/view_file.html', {'file': file_obj, 'password_required': True})

    return render(request, 'core/view_file.html', {'file': file_obj})

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        password = request.POST.get('password')
        expiry_hours = request.POST.get('expiry')

        expires_at = None
        if expiry_hours:
            expires_at = timezone.now() + timedelta(hours=int(expiry_hours))

        file = SharedFile.objects.create(
            file=uploaded_file,
            password=password,
            expiry=expires_at
        )

        shareable_link = request.build_absolute_uri(
            reverse('view_file', args=[file.uuid])
        )
        
        return render(request, 'core/file_uploaded.html', {'shareable_link': shareable_link})

    return render(request, 'core/upload.html')

def serve_file(request, file_uuid):
    file_obj = get_object_or_404(SharedFile, uuid=file_uuid)
    if file_obj.expiry and timezone.now() > file_obj.expiry:
        raise Http404("This file has expired.")
    if file_obj.password:
        password = request.GET.get('password')
        if password != file_obj.password:
            return HttpResponseForbidden("Incorrect password.")
    return FileResponse(file_obj.file, as_attachment=True)

def delete_file(request, file_uuid):
    file_obj = get_object_or_404(SharedFile, uuid=file_uuid)

    if request.method == "POST":
        if file_obj.file:
            file_obj.file.delete(save=False)
        file_obj.delete()
        messages.success(request, "File deleted successfully!")
        return redirect('home') 

    return render(request, 'core/confirm_delete.html', {'file': file_obj})
