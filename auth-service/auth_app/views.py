from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .controllers import AuthController

class RegisterUserView(APIView):
    def post(self, request):
        user, error = AuthController.register_user(
            request.data.get('username'),
            request.data.get('email'),
            request.data.get('password')
        )
        if error:
            return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'User registered', 'user_id': user.id}, status=status.HTTP_201_CREATED)