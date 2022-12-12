from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import PerevalView


urlpatterns = [
    path('', PerevalView.as_view({'post': 'submit_data', 'get': 'list_for_user'})),
    path('<int:pk>', PerevalView.as_view({'get': 'get_record', 'patch': 'update_record'})),
]
