from django.urls import path

from main.views import upload_view, result_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', upload_view, name='home'),
    path('result', result_view, name='result')
]
urlpatterns += staticfiles_urlpatterns()