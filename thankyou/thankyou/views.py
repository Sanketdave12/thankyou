from django.shortcuts import HttpResponse, render

def thankyou(request):
    return render(request, 'thankyou.html')