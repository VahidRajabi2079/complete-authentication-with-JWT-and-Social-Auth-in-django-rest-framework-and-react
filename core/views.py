from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from . import serializers, utils, models


class RegisterUser(GenericAPIView):
    serializer_class = serializers.UserRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            # send email function user['email]
            utils.send_code_to_user(user["email"])
            return Response(
                {
                    "data": user,
                    "message": f"hi thanks for signing up a passcode has be sent to verifiy your email",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail(GenericAPIView):
    serializer_class = serializers.VerifyEmailSerializer

    def post(self, request):
        otpcode = request.data.get("otp")
        try:
            user_code_obj = models.OneTimePassword.objects.get(code=otpcode)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(
                    {"message": "aacount email verified successfully"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "code is invalid user alread verified"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except models.OneTimePassword.DoesNotExist:
            return Response(
                {"message": "passcode note provided"}, status=status.HTTP_404_NOT_FOUND
            )


class LoginUserView(GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestAuthenticationView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {"msg": "its works"}
        return Response(data, status=status.HTTP_200_OK)


class PassWordResetRequestView(GenericAPIView):
    serializer_class = serializers.PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "a link has been send to your email to reset your password"},
            status=status.HTTP_200_OK,
        )


class PsswordReserConfirm(GenericAPIView):
    def get(self, requets, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = models.CustomUser.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {"message": "token is invalid or has expi"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            return Response(
                {
                    "sucess": True,
                    "message": "credentials is valid",
                    "uidb64": uidb64,
                    "token": token,
                },
                status=status.HTTP_200_OK,
            )

        except DjangoUnicodeDecodeError:
            return Response(
                {"message": "token is invalid or has expi"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class SetNewPassword(GenericAPIView):
    serializer_class = serializers.SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "password reset successfull"}, status=status.HTTP_200_OK
        )


class LogoutUserView(GenericAPIView):
    serializer_class = serializers.LogoutUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
