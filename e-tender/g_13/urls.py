"""g_13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from tender import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	
	url(r'^$',views.home,name='home'),
	url(r'^requesting/(?P<user_data>\w+)/$',views.requesting,name='requesting'),
	#url(r'^bidnow/(?P<pk_t>\d+)/(?P<s>\s*)/$',views.bid_now2,name='bid_now2'),
	url(r'^bidnow/(?P<pk_t>\d+)/(?P<comp_name>\w+)/$',views.bid_now,name='bid_now'),
	url(r'^complaints/$',views.complaints,name='complaints'),
	url('^admin/',admin.site.urls),
	url(r'^sub_departments/(?P<pk>\d+)/$',views.sub_departments,name='sub_departments'),
	url(r'^tenders/(?P<pk>\d+)/$',views.tenders,name='tenders'),
	url(r'^signup/$',accounts_views.signup,name='signup'),
	url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^bid/(?P<pk>\d+)/$',views.bid,name='bid'),
]
# this file contains the urls of all the references


# home -- default home page
# requesting -- it asks for company registeration number
# bid_now -- displays a form which takes the input the bidding price and description
# complaints -- it is a form which accepts all the complaints
# admin -- it is the url for admin login
# sub_departments -- it is the page obtained on clicking dept name which lists all the subdept under that dept
# tenders -- it displays all the tenders under a particular subdept
# signup -- for signing up
# login - for login purpose
# bid -- it shows all the bids of a particular tender