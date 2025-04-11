from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('predict/', views.predict_view, name='predict'),
    path('result/<str:name>/<str:result>/', views.result_view, name='result'),
]
