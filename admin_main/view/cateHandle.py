from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def cate(request):
    return render_to_response('cateView/cate.html')
