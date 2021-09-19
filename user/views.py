from .models import UserData, User
from rest_framework import generics,  authentication, permissions, serializers, viewsets
from user.serializers import UserDataSerializer, UserSerializer, AuthTokenSerializer, UserDataSerializer  \
                                , UserLeaderBoardSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


# class CreateAdminUserView(generics.CreateAPIView):
#     """Create a new user in the system"""
#     serializer_class = AdminUserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserDataView(APIView):
    """View for UserData"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        userId = self.request.user
       # print('THSISISISISIISI USER',userId)
        queryset  = UserData.objects.get(user=userId)
        #print('NICEEEEEEEEEEEEEEEEEEE',queryset)
        serializer =  UserDataSerializer(queryset)
        #print(serializer)
        return Response(serializer.data)

class UserLeaderBoardView(APIView):
    """Listing Users... points"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, queryset, format=None):
        queryset = UserData.objects.all().order_by('-points')
        serializer = UserLeaderBoardSerializer(queryset, many=True)
        print('wowowow', serializer)
        return Response(serializer.data)