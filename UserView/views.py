from django.shortcuts import render
from .models import Video, Package,HomeVideo, Videographer
def index(request):
    videos = Video.objects.all()
    video = HomeVideo.objects.all()[0]
    videographers = Videographer.objects.all()
    return render(request, 'UserView/home.html', {'videos':videos,
                                                   'packages':packages,
                                                    'video':video,
                                                    'videographers':videographers})

def packages(request):
    packages = Package.objects.all()
    return render(request,'UserView/packages.html', {'Packages':packages})

def videography(request):
    packages = Package.objects.filter(field='videography')
    return render(request,'UserView/packages.html', {'Packages':packages})
def cinematography(request):
    packages = Package.objects.filter(field='cinema')
    return render(request,'UserView/packages.html', {'Packages':packages})