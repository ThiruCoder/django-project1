from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from home.views import *

urlpatterns = [
    path('',home,name='home'),
    path('upload/',uploadData,name='upload'),
    path('update/<int:id>',updateData,name='update'),
    path('delete/<int:id>',deleteData,name='delete'),

]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

