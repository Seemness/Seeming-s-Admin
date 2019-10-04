from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response


@login_required
def admin_list(request):
    return render_to_response('adminView/admin-list.html')


@login_required
def admin_role(request):
    return render_to_response('adminView/admin-role.html')


@login_required
def admin_cate(request):
    return render_to_response('adminView/admin-cate.html')


@login_required
def admin_rule(request):
    return render_to_response('adminView/admin-rule.html')
