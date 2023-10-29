from django.urls import path

from . import views

app_name = "riezas_travel"  # URL namespacing

urlpatterns = [
    path("", views.index, name="index"),
]
