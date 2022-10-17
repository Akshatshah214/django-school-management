from django.urls import path
from .views import (
    PersonDataDetailView,
)

urlpatterns = [
    path(
        "person_data", PersonDataDetailView.as_view(), name="person_data_list"
    ),
    path(
        "person_data/<int:pk>",
        PersonDataDetailView.as_view(),
        name="person_data_list",
    ),
]
