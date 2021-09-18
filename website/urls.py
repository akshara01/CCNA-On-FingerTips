from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('module',views.module,name = 'module'),
    path('dynamic/<str:model_class>?<str:mod_no>?<str:sub_modno>',views.dynamic,name = 'dynamic'),
    path('module2',views.module2,name = 'module2'),
    path('module3',views.module3,name = 'module3'),
    path('module4',views.module4,name = 'module4'),
    path('module5',views.module5,name = 'module5'),
    path('module6',views.module6,name = 'module6'),
    path('module6',views.module6,name = 'module6'),
    path('search',views.search,name = 'search'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)