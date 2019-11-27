"""SMW URL Configuration

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
from shop import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url('^admin/',admin.site.urls),
    url('^ware_houses_login/$',views.ware_house_login,name='ware_house_login'),
    url('^trucks_login/$',views.truck_login,name='truck_login'),
    url('^ware_home/(?P<pk>\d+)/$',views.ware_home,name='ware_home'),
    url('^ware_details/(?P<option>\d+)/(?P<pk>\d+)/$',views.ware_details,name='ware_details'),
    url('^truck_home/(?P<pk>\d+)/$',views.truck_home,name='truck_home'),
    url('^billing/(?P<pk_c>\d+)/(?P<pk_t>\d+)/$',views.billing,name='billing'),
    url('^procure_customer/(?P<pk_t>\d+)/$',views.procure_customer,name='procure_customer'),
    url('^procure_item_list/(?P<pk>\d+)/(?P<pk_t>\d+)/$',views.procure_item_list,name='procure_item_list'),
    url('^update_quantity_ware/(?P<pk_i>\d+)/(?P<pk_w>\d+)/$',views.update_quantity_ware,name='update_quantity_ware'),
    url('^selling_item_list/(?P<pk>\d+)/(?P<pk_t>\d+)/(?P<final_total>\d+)/$',views.selling_item_list,name='selling_item_list'),
    url('^selling_customer/(?P<pk_t>\d+)/$',views.selling_customer,name='selling_customer'),
    url('^sell_billing/(?P<pk_t>\d+)/(?P<pk_c>\d+)/(?P<tot>\d+)/$',views.sell_billing,name='sell_billing'),
    url('^truck_items/(?P<pk_t>\d+)/$',views.truck_items,name='truck_items'),
]
