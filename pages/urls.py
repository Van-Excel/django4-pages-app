from django.urls import path
from .views import HomePage, AboutPage


# urlpatterns

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view())
]
