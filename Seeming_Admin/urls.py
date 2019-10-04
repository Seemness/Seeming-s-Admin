"""Seeming_Admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
import admin_main.view.userHandle as userHandle
import admin_main.view.orderHandle as orderHandle
import admin_main.view.cateHandle as cateHandle
import admin_main.view.cityHandle as cityHandle
import admin_main.view.adminHandle as adminHandle
import admin_main.view.echartsHandle as echartsHandle
import admin_main.view.unicodeHandle as unicodeHandle
import admin_main.view.otherHandle as otherHandle

urlpatterns = [
    # ---------------------- userHandle  URLS-----------------------------#
    path('', userHandle.login_auth, name='login'),
    path('login', userHandle.login_auth, name='login'),
    path('register', userHandle.register_auth, name='register'),
    path('index', userHandle.index, name='index'),
    path('logout', userHandle.logout_auth, name='logout'),
    path('member-list', userHandle.member_list, name='member-list'),
    path('member-list1', userHandle.member_list1, name='member-list1'),
    path('member-add', userHandle.member_add, name='member-add'),
    path('member-del', userHandle.member_del, name='member-del'),
    path('member-del2', userHandle.member_del2, name='member-del2'),
    path('update-psd', userHandle.update_psd, name='update-psd'),
    path('member-del-count', userHandle.del_member_count, name='member-del-count'),
    path('welcome', userHandle.welcome, name='welcome'),
    path('error', userHandle.error, name='error'),

    # ---------------------- orderHandle  URLS-----------------------------#
    path('order-list', orderHandle.order_list, name='order-list'),
    path('order-add', orderHandle.order_add, name='order-add'),

    # ---------------------- cateView  URLS-----------------------------#
    path('cate', cateHandle.cate, name='cate'),

    # ---------------------- cityView  URLS-----------------------------#
    path('city', cityHandle.city, name='city'),

    # ---------------------- adminView  URLS-----------------------------#
    path('admin-list', adminHandle.admin_list, name='admin-list'),
    path('admin-role', adminHandle.admin_role, name='admin-role'),
    path('admin-cate', adminHandle.admin_cate, name='admin-cate'),
    path('admin-rule', adminHandle.admin_rule, name='admin-rule'),

    # ---------------------- echartsView  URLS-----------------------------#
    path('echarts1', echartsHandle.echarts1, name='echarts1'),
    path('echarts2', echartsHandle.echarts2, name='echarts2'),
    path('echarts3', echartsHandle.echarts3, name='echarts3'),
    path('echarts4', echartsHandle.echarts4, name='echarts4'),
    path('echarts5', echartsHandle.echarts5, name='echarts5'),
    path('echarts6', echartsHandle.echarts6, name='echarts6'),
    path('echarts7', echartsHandle.echarts7, name='echarts7'),
    path('echarts8', echartsHandle.echarts8, name='echarts8'),

    # ---------------------- echartsView  URLS-----------------------------#
    path('unicode', unicodeHandle.unicode, name='unicode'),

    # ---------------------- otherView  URLS-----------------------------#
    path('demo', otherHandle.demo, name='demo'),
    path('log', otherHandle.log, name='log'),
]
