from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response


@login_required
def demo(request):
    return render_to_response('otherView/demo.html')


@login_required
def log(request):
    return render_to_response('otherView/log.html')
