from django.urls import path, include
from file_upload import settings
from django.conf.urls.static import static
from file_receive import views
from file_receive.views import hotel_image_view, success

urlpatterns = [ 
    path('image_upload/', hotel_image_view, name = 'image_upload'), 
    path('success/', success, name = 'success'), 
    path('form/', views.Form),
    path('upload/', views.Upload),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
