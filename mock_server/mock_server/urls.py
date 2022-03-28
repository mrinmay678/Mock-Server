from django.urls import path
from .views import MockServerView

urlpatterns = [
    path('<service>', MockServerView.as_view()),
]
