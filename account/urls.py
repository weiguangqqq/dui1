# -*- coding: utf-8 -*-
#
#from django.conf.urls import url    
#from . import views    
#
#urlpatterns = [        
#    # post views        
#    url(r'^login/$', views.user_login, name='login'),    
#]

from django.conf.urls import url
from django.contrib.auth.views import login
# With django 1.10 I need to pass the callable instead of 
# url(r'^login/$', 'django.contrib.auth.views.login', name='login')

from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_change
from . import views


urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),
# login logout
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    # change password
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
    # reset password
    ## restore password urls
    url(r'^password-reset/$',
    	password_reset,
		name='password_reset'),
    url(r'^password-reset/done/$',
		password_reset_done,
		name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
		password_reset_confirm,
		name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
		password_reset_complete,
		name='password_reset_complete'),
        
    url(r'^$', views.dashboard, name='dashboard'),

#改密码
    url(r'^password-change/$',
   password_change,
   name='password_change'),
    url(r'^password-change/done/$',
   password_change,
   name='password_change_done'),

#注册
    url(r'^register/$', views.register, name='register'),
    url(r'^shouji/$', views.shouji, name='shouji'),
    url(r'^shuben/$', views.shuben, name='shuben'),
    url(r'^upan/$', views.upan, name='upan'),
    url(r'^zhengjian/$', views.zhengjian, name='zhengjian'),
    url(r'^yusan/$', views.yusan, name='yusan'),
    url(r'^qita/$', views.qita, name='qita'),
    
    #失物招领
    url(r'^sxiaoyuanka/$', views.sxiaoyuanka, name='sxiaoyuanka'),
    url(r'^sshouji/$', views.sshouji, name='sshouji'),
    url(r'^sshuben/$', views.sshuben, name='sshuben'),
    url(r'^supan/$', views.supan, name='supan'),
    url(r'^szhengjian/$', views.szhengjian, name='szhengjian'),
    url(r'^syusan/$', views.syusan, name='syusan'),
    url(r'^sqita/$', views.sqita, name='sqita'),
    url(r'^xiaoli/$', views.xiaoli, name='xiaoli'),
    url(r'^zuoxibiao/$', views.zuoxibiao, name='zuoxibiao'),
    url(r'^lifein/$', views.lifein, name='lifein'),
    url(r'^taolunqu/$', views.taolunqu, name='taolunqu'),
    
    ]

