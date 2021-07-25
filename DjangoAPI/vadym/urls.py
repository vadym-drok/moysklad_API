from .views import orderApi
from django.conf.urls import url

urlpatterns=[
    url(r'^orders$', orderApi),
    url(r'^orders/([0-9]+)$', orderApi),
]