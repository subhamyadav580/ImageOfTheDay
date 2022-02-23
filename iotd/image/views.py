from django.shortcuts import render, redirect
from .models import FeaturedImage
from .forms import ImageUploadForm

def home(request):
    if request.method == 'GET':
        form = ImageUploadForm()
        return render(request, 'images/image_upload.html', {"form" : form})
    elif request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("latestImage")
        else:
            form = ImageUploadForm()
            return render(request, 'images/image_upload.html', {"form" : form})


def latestImage(request):
    images = FeaturedImage.objects.all().order_by("-uploaded")
    if not images:
        return redirect("home")
    else:
        image = images[0]
        return render(request ,'images/home.html',
                                { 'image' : image})