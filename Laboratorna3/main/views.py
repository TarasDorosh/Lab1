import time
from django.shortcuts import render
from django.http import JsonResponse
import os


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
        response = dict(date= time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()), current_page=request.path, server_info=os.name, client_info=os.uname()[1])
        return JsonResponse(response)
