from django.shortcuts import render
from .forms import VideoForm
from django.contrib import messages
from .models import Video
def home(request):
    app_name = 'Philosophy Videos' # video category
    return render(request, 'video_collection/home.html', {'app_name':app_name})

def add(request):
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.info(request, 'New video save!')
        else:
            messages.warning(request, 'Please check the data entered.')
            return render(request, 'video_colelction/add.html',{'new_video_form':new_video_form})
        
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list (request):
    videos = Video.object.all()
    return render(request, 'video_collection/video_list.html', {'videos':videos})




