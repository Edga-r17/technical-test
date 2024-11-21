from django.urls import path
from .views import MissingNumberView

urlpatterns = [
    path('find-missing-number/', MissingNumberView.as_view(), name='MissingNumberView'),
]
