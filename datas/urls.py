from django.urls import path
from datas import views
from django.contrib.auth.views import login,logout

urlpatterns=[
path('',views.start,name='start'),
path('accounts/profile/home/',views.home,name='home'),
path('login1/', views.login1,  name='login1'),
path('login2/', views.login2, name='login1'),
path('accounts/profile/logout.html/', logout, {'template_name': 'datas/logout.html'}),
path('register/', views.register, name='register'),
path('accounts/profile/', views.profile, name='profile'),
path('profile/check/',views.check,name='check'),
path('accounts/profile/home1/',views.home1,name='home1'),
path('accounts/profile/home2/',views.home2,name ='home2'),
path('accounts/profile/home3/',views.home3,name ='home3'),
path('accounts/profile/home/menu',views.menu,name='menu'),
path('accounts/profile/home/order',views.order,name='order'),
path('select1/',views.select1,name ='select1'),
]