from django.urls import path
from .views import category, home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', home, name="home"),
    path('category/', category),

]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
