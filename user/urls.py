from django.urls import path

from user import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    # path('create-admin/', views.CreateAdminUserView.as_view(), name='create-admin'),
    path('token/', views.CreateTokenView.as_view(), name='token'), 
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('user-data/', views.UserDataView.as_view(), name='user-data'),
    path('leaderboard/', views.UserLeaderBoardView.as_view(), name='leaderboard'),
]