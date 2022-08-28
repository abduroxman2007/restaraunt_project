from rest_framework import serializers
from .models import *


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'image', 'location', 'description']


class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]


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
