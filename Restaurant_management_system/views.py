# I have created this file - Darshan
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def Profile(request):
    if request.method == "POST":
        current = request.POST.get("cpass")
        new_pass = request.POST.get("npass")
        user = User.objects.get(id=request.user.id)
        un = user.username
        pwd = new_pass
        check = user.check_password(current)
        if check == True:
            user.set_password(new_pass)
            user.save()
            return HttpResponse("Password Changed Successfully:)")
            user = User.objects.get(username=un)
            login(request, user)
        else:
            return HttpResponse("Current Password is incorrect!!!")
    return render(request, 'Profile.html')
