from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import random
import math
import sys
from decimal import *

def simple(request):
    """
    generate simple cpu running load
    """
    a = Decimal(1.0)
    b = Decimal(1.0/math.sqrt(2))
    t = Decimal(1.0)/Decimal(4.0)
    p = Decimal(1.0)

    for i in range(2048):
        at = Decimal((a+b)/2)
        bt = Decimal(math.sqrt(a*b))
        tt = Decimal(t - p*(a-at)**2)
        pt = Decimal(2*p)

        a = at;b = bt;t = tt;p = pt

    my_pi = (a+b)**2/(4*t)
    accuracy = 100*(Decimal(math.pi)-my_pi)/my_pi

    return HttpResponse(my_pi)
