from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response


@login_required
def order_list(request):
    return render_to_response('orderView/order-list.html')


@login_required
def order_add(request):
    return render_to_response('orderView/order-add.html')
