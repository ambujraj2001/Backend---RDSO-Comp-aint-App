from django.urls import path,re_path
#from django.conf.urls import  url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    #path('login/(?P<value>\d+)/$',views.forgetPassword,name='login')
    #re_path(r'^forgetpass/(?P<user_id>\d+)/$', views.forgetPassword, name='urlname'),
    re_path(r'^generateotp/(?P<user_id>\d+)/$', views.generateotp, name='urlname'),
    re_path(r'^getotp/(?P<user_id>\d+)/$', views.getotp, name='urlname'),
    re_path(r'^reset/(?P<user_id>\d+)/$', views.resetpassword, name='urlname'),
    re_path(r'^updates/(?P<user_id>\d+)/$', views.updates, name='urlname'),
    re_path(r'^update/(?P<user_id>\d+)/$',views.update, name='urlname'),
    re_path(r'^getempdetail/(?P<login_id>\d+)/$',views.getempdetail, name='urlname'),
    re_path(r'^bldg/', views.getbldg, name='designation'),
    re_path(r'^dte/', views.directorate, name='designation'),
    re_path(r'^setdetail/(?P<login_id>\d+)/$', views.setdetail, name='designation'),
    re_path(r'^pay/', views.paylevel, name='designation'),
    re_path(r'^basic/(?P<levelname>\w+)/$', views.basic, name='designation'),
    re_path(r'^sendsms/', views.sendsms, name='designation'),
    re_path(r'^sendemail/', views.sendemail, name='designation'),
    re_path(r'^changepassword/(?P<userid>\d+)/$', views.changepassword, name='designation'),
    re_path(r'^getmenuid/(?P<id>\d+)/$', views.getmenuid, name='designation')
]

