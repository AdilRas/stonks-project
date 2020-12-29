from django.urls import path, include
from .views import TestView, StockView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('test/', TestView.as_view()),
    path('stock/', StockView.as_view())
]

