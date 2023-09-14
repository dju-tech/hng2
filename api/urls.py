from django.urls import path

from .views import (
  PersonViewList,
  PersonViewDetail
)

urlpatterns = [
  path('api/', PersonViewList.as_view()),
  path(r'api/<str:pk_or_name>/', PersonViewDetail.as_view())
]