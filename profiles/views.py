from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

# def profile_view(request):
#     profile = Profile.objects.get(user=request.user)
#     return render(request, 'profile.html', {
#         'user': request.user,
#         'profile': profile
#     })

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profiles/profile.html', {
        'user': request.user,
        'profile': profile
    })


def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profiles/profile.html', {
        'user': request.user,
        'profile': profile
    })
