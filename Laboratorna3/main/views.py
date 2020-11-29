import time
from django.shortcuts import render
from django.http import JsonResponse
import os


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
        response = dict(date= time.strftime("%d %b %Y %H:%M:%S", time.gmtime()),
                        current_page=request.build_absolute_uri(),
                        server_info=os.uname().sysname,
                        client_info=os.getlogin())
        return JsonResponse(response)
