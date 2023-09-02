from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegistrationSerializer, ActivationSerializer,LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .permission import IsActivePermission
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import ForgotPasswordSerializer, ForgotPasswordCompleteSerializer
from django.core.mail import send_mail
from .models import User
import logging

User = get_user_model()


logger = logging.getLogger(__name__)

# def my_view(request):
#     logger.debug('Это сообщение отладки')
#     logger.info('Информационное сообщение')
#     logger.warning('Предупреждение')
#     logger.error('Ошибка')
#     logger.critical('Критическая ошибка')



class RegistrationView(APIView):

    
    def post(self, request):
        serializer = RegistrationSerializer(
            data=request.data
        )
        logger.info('Информационное сообщение')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Аккаунт успешно создан', status=201)
    

class ActivationView(APIView):

    def post(self, request):
        serializer = ActivationSerializer(
            data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response(
                'Аккаунт успешно активирован',
                status=200
            )


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutView(APIView):
    permission_classes= [IsActivePermission]
    def post(self,request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли из своего аккаунта')




# class ForgotPasswordView(generics.CreateAPIView):
#     serializer_class = ForgotPasswordSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         user_data = serializer.validated_data
#         user = User.objects.get(email=user_data['email'],username=user_data['name'])
#         user.create_activation_code()
#         user.save()

#         send_mail(
#             'Восстановление пароля',
#             f'Ваш код восстановления: {user.activation_code}',
#             'example@gmail.com',
#             [user.email]
#         )

#         return Response({'message': 'Код восстановления отправлен на ваш email.'}, status=status.HTTP_200_OK)
class ForgotPasswordView(generics.CreateAPIView):
    serializer_class = ForgotPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_data = serializer.validated_data
        email = user_data['email']

        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()

        send_mail(
            'Восстановление пароля',
            f'Ваш код восстановления: {user.activation_code}',
            'example@gmail.com',
            [user.email]
        )

        return Response({'Код восстановления отправлен на ваш email.'}, status=status.HTTP_200_OK)


class ForgotPasswordCompleteView(generics.CreateAPIView):
    serializer_class = ForgotPasswordCompleteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.validated_data
        email = user_data['email']
        activation_code = user_data['code']

        user = User.objects.get(email=email, activation_code=activation_code)
        user.set_password(user_data['password'])
        user.activation_code = ''
        user.save()

        return Response({'Пароль успешно изменен.'}, status=status.HTTP_200_OK)

