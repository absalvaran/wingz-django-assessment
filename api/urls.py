from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rides import views as rides
from users import views as users
from knox.views import LogoutView as KnoxLogoutView
from debug_toolbar.toolbar import debug_toolbar_urls


router = routers.DefaultRouter()
router.register(r"rides", rides.RideView, "rides")
router.register(r"ride-events", rides.RideEventView, "ride-events")
router.register(r"users", users.UserView, "users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/login/", users.LoginView.as_view()),
    path("api/logout/", KnoxLogoutView.as_view()),
] + debug_toolbar_urls()
