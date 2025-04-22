from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("verify-email/", views.VerifyUserEmail.as_view(), name="verify"),
    path('login/',views.LoginUserView.as_view(),name='login'),
    path('profile/',views.TestAuthenticationView.as_view(),name='granted'),
    path('token/refresh',TokenRefreshView.as_view(),name='refresh-token'),
    path('password-reset/',views.PassWordResetRequestView.as_view(),name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>',views.PsswordReserConfirm.as_view(),name='password-reset-confirm'),
    path('set-new-password/',views.SetNewPassword.as_view(),name='set-new-password'),
    path('logout/',views.LogoutUserView.as_view(),name='logout'),
    
]
