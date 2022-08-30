from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from .models import *


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'image', 'location', 'description']


class DjangoUserSerializer(serializers.ModelSerializer):

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username already taken')

        return username
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

# class RegisterUserSerializer(Serializer):
#     username = CharField(max_length=255)
#     password = CharField(max_length=255)
#
#     def validate_username(self, username):
#         if User.objects.filter(username=username).exists():
#             raise ValidationError('This username already taken')
#
#         return username
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
#
#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         user = User(**validated_data)
#         user.save()
#         return user


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'image', 'phone_number']


class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'image',
            'description',
            'price',
            'rate',
        ]


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = [
            'id',
            'people_size',
            'image',
            'number',
            'part',
            'branch',
        ]


class TableOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOrder
        fields = [
            'id',
            'branch',
            'table',
            'order_date',
            'create_date',
            'status',
            'client',
        ]


class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = [
            'id',
            'table_order',
            'food',
            'count',
        ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id',
            'food',
            'rating',
        ]
