from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, render_to_response
from ..models import user
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required  # 验证是否登录的中间件
import json


# def register(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('name')
#         user_password = request.POST.get('password')
#         user_email = request.POST.get('email')
#         check_user = User.objects.create_user(username=user_name, password=user_password, email=user_email)
#         if check_user:
#             return HttpResponse(json.dumps({'status': 200, 'message': 'success'}),
#                                 content_type="application/json,charset=utf-8")


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_password = request.POST.get('password')
        check_user = user.User.objects.filter(user_name=user_name, user_password=user_password)
        if check_user:
            response = HttpResponseRedirect('/index')
            response.set_cookie('username', user_name, 3600)
            return response
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@login_required
def index(request):
    return render(request, 'index.html')


def register_auth(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_password = request.POST.get('password')
        user_email = request.POST.get('email')
        check_user = User.objects.create_user(username=user_name, password=user_password, email=user_email)
        if check_user:
            return HttpResponse(json.dumps({'code': 200, 'message': 'success'}),
                                content_type="application/json,charset=utf-8")
        else:
            return HttpResponse(json.dumps({'code': 400, 'message': 'failed'}),
                                content_type="application/json,charset=utf-8")


def login_auth(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_password = request.POST.get('password')
        print(user_name)
        print(user_password)
        check_user = auth.authenticate(username=user_name, password=user_password)
        if check_user:
            auth.login(request, check_user)
            return redirect('/index')
        else:
            # msg = {'登录失败！'}
            # return render(request, 'login.html')
            return JsonResponse({'code': 300, 'message': 'failed'})
            # return JsonResponse({'code': 300, 'message': 'failed'})
    else:
        return render(request, 'login.html')


def logout_auth(request):
    auth.logout(request)
    return redirect('/login')


@login_required
def member_list(request):
    all_user = User.objects.all().values('username', 'email', 'id')
    # u_dict = json.loads(serializers.serialize('json', all_user))
    # return render(request, 'member-list.html', )
    return render_to_response('userView/member-list.html', {'current_date': all_user})


@login_required
def member_add(request):
    return render_to_response('userView/member-add.html')


@login_required
def member_del(request):
    if request.method == 'GET':
        user_name = request.GET.get('name', default='')
        user_id = request.GET.get('id', default='')
        if not all([user_name, user_id]):
            return JsonResponse({'code': 1, 'message': '数据不完整'})
        try:
            User.objects.get(username=user_name, id=user_id).delete()
        except User.DoesNotExist:
            msg = {'code': 300, 'message': 'failed'}
            return JsonResponse(msg)
        else:
            return HttpResponse(json.dumps({'code': 200, 'message': 'success'}),
                                content_type="application/json,charset=utf-8")


@login_required
def update_psd(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        new_psd = request.POST.get('psd')
        if not all([user_id, new_psd]):
            return JsonResponse({'code': 1, 'message': '数据不完整'})
        try:
            u = User.objects.get(id=user_id)
            u.set_password(new_psd)
            u.save()
        except User.DoesNotExist:
            msg = {'code': 300, 'message': 'failed'}
            return JsonResponse(msg)
        return JsonResponse({'code': 200, 'message': 'success'})


@login_required
def del_member_count(request):
    if request.method == 'POST':
        user_id = request.POST.getlist('id[]')  # 用ajax提交的数组即{‘id':[4,5,6]},  getlist的参数后要加[]
        # if not all([user_id]):
        #     return JsonResponse({'code': 1, 'message': '数据不完整'})
        try:
            for i in user_id:
                u = User.objects.get(id=i)
                u.delete()
        except User.DoesNotExist:
            msg = {'code': 300, 'message': 'failed'}
            return JsonResponse(msg)
        else:
            return JsonResponse({'code': 200, 'message': 'success'})


@login_required
def welcome(request):
    return render_to_response('userView/welcome.html')


def error(request):
    return render_to_response('userView/error.html')


def member_list1(request):
    return render_to_response('userView/member-list1.html')


def member_del2(request):
    return render_to_response('userView/member-del.html')
