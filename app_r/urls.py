from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='homepage'),
    path('about/', views.home,name='aboutpage'),
    path('search/',views.search,name = 'search'),
    path('add/',views.add_project,name = 'add_project'),
    path('review/',views.review,name = 'review'),
    # create API endpoint
    path('project/', views.ProjectListApi().as_view()), 
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)