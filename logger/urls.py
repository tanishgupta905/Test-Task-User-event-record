from django.urls import path
from .views import UserActivityView


urlpatterns = [
    path('user/<str:username>/activity', UserActivityView.as_view(), name='user-activity'),
]