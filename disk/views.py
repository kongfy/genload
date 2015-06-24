from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import tempfile

STRS = ['0123456789abcdefghijklmnopqrstuvwxyz'] * 1000

def simple(request):
    """
    generate simple disk running load
    """

    f = tempfile.TemporaryFile(mode='r+w')
    f.writelines(STRS)
    for line in f:
        pass
    f.close()

    return HttpResponse('OK')
