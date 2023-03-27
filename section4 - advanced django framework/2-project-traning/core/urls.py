from django.urls import path
# from .views import IndexView, TesteView, TesteTwoView
from .views import IndexView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
    # path('teste/', TesteView.as_view(), name='teste'),
    # path('teste2/', TesteTwoView.as_view(), name='teste2'),
]
