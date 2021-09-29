import cv2
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = (
    path('', views.index, name='home'),
    # path('', views.test, name='test'),
    path('info', views.info, name='info'),
    path('error', views.error, name='error'),
    # path('test', views.test, name='test'),
    path('result', views.result, name='result'),
    path('printinfo', views.printinfo, name='printinfo'),
    path('getDataPhoto', views.getDataPhoto, name='getDataPhoto'),
    # path(r'?P<'/url/to/ajax/view/(?P<some_data>[\w-]+)/$', views.my_ajax_view),
)
