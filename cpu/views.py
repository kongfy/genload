from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import random
import math
import sys

def simple(request):
    """
    generate simple cpu running load
    """
    for i in range(128):
        n = random.randint(0, sys.maxint)
        n = math.sqrt(n)

    return HttpResponse('')
