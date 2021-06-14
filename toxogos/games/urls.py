from rest_framework import routers
from django.urls import path, include
from games import views

app_name = "games"

router = routers.SimpleRouter()

router.register(r"games", views.GameViewSet, basename="games")

urlpatterns = [
    path('', include(router.urls)),
]
