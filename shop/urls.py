from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'/', views.main_view),
    url(r'/news', views.news),
]
