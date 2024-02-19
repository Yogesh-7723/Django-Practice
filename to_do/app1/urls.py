from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index),
    path('addtask/',views.addtask),
   # path('success/<int:uid>/',views.success,name='success'),
    path('delete/<int:uid>/',views.delete),
    path('success/<int:qk>/',views.success,name='success'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

