from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def echarts1(request):
    return render_to_response('echartsView/echarts1.html')


@login_required
def echarts2(request):
    return render_to_response('echartsView/echarts2.html')


@login_required
def echarts3(request):
    return render_to_response('echartsView/echarts3.html')


@login_required
def echarts4(request):
    return render_to_response('echartsView/echarts4.html')


@login_required
def echarts5(request):
    return render_to_response('echartsView/echarts5.html')


@login_required
def echarts6(request):
    return render_to_response('echartsView/echarts6.html')


@login_required
def echarts7(request):
    return render_to_response('echartsView/echarts7.html')


@login_required
def echarts8(request):
    return render_to_response('echartsView/echarts8.html')
