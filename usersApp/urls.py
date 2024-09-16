from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usersApp.apps import UsersappConfig
from usersApp.views.users import Registration

app_name = UsersappConfig.name

urlpatterns = [
    # users
    path('create/', Registration.as_view(), name='user-create'),

    # token urls
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='access-token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token-refresh'),
]
