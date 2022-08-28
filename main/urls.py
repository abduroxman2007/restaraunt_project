from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [

    path('chekorders/', chekorders, name='chekorders'),

    path('branchlist/', BranchAPIView.as_view(), name='branchlist'),
    path('branchlist/<int:pk>/', BranchAPIUpdate.as_view(), name='branchlistupdate'),

    path('userlist/', UserAPIView.as_view(), name='userlist'),
    path('userlist/<int:pk>/', UserAPIView.as_view(), name='userlistupdate'),

    path('clientlist/', ClientAPIView.as_view(), name='clientlist'),
    path('clientlist/<int:pk>/', ClientAPIUpdate.as_view(), name='clientlistupdate'),

    path('foodslist/', FoodsAPIView.as_view(), name='foodslist'),
    path('foodslist/<int:pk>/', FoodsAPIUpdate.as_view(), name='foodslistupdate'),

    path('tablelist/', TableAPIView.as_view(), name='tablelist'),
    path('tablelist/<int:pk>/', TableAPIUpdate.as_view(), name='tablelistupdate'),

    path('tableorderlist/', TableOrderAPIView.as_view(), name='tableorderlist'),
    path('tableorderlist/<int:pk>/', TableOrderAPIUpdate.as_view(), name='tableorderlistupdate'),

    path('orderfoodlist/', OrderFoodAPIView.as_view(), name='orderfoodlist'),
    path('orderfoodlist/<int:pk>/', OrderFoodAPIUpdate.as_view(), name='orderfoodlistupdate'),

    path('reatinglist/',RatingAPIView.as_view(), name='reatinglist'),
    path('reatinglist/<int:pk>/', RatingAPIUpdate.as_view(), name='reatinglistupdate'),

    #  Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
