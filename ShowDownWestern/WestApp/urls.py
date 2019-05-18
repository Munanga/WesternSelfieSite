from django.conf.urls import url
from WestApp import views

app_name = 'WestApp'

urlpatterns = [
    url(r'^$',views.upload,name='upload'),
]