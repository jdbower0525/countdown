from django.conf.urls import url
from countdownapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
