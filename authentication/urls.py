from django.urls import path,include
from .views import *
# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )
urlpatterns =[
    path('register/',RegisterView.as_view(),name="register"),
    # path('email-verify/<int:id>/',VerifyEmail.as_view(),name="email-verify"),
    path('login/',LoginAPI.as_view(),name="login"),
    # path('password-reset/<uidb64>/<token>/',SetNewPasswordAPI.as_view(),name="password-reset-confirm"),
    # path('request-reset-password/',RequestPasswordResetEmail.as_view(),name="request-reset-password"),
    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('password_reset/',SetNewPasswordAPI.as_view(),name="password-reset"),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('user-details/',UserDetailsCreate.as_view(),name="user_details"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name="password-reset-confirm")
]