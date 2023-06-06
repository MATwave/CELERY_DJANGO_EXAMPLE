from django.urls import path

from .views import ContactView
from .views import HealthCheckView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('health', HealthCheckView.as_view(), name='health')
]
