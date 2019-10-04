from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response


@login_required
def unicode(request):
    return render_to_response('unicodeView/unicode.html')
