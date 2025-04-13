from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rides import views as rides
from users import views as users

router = routers.DefaultRouter()
router.register(r"rides", rides.RideViews, "rides")
router.register(r"ride-events", rides.RideEventViews, "ride-events")
router.register(r"users", users.UserViews, "users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
