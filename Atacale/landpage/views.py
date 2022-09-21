from django.shortcuts import render


def land(request):
       
    return render(request, 'landpage/index.html', {})