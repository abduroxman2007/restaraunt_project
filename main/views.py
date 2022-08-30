from datetime import datetime
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

def chekorders(request):
    now = datetime.now()
    if request.method == 'GET':
        for item in TableOrder.objects.filter(order_date__lte=now):
            item.status = False
            item.save()


#                                Branch
class BranchAPIView(ListCreateAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        return Branch.objects.filter(**self.request.GET.dict())


class BranchAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


#                                Django User


class UserAPIView(ListCreateAPIView):
    serializer_class = DjangoUserSerializer

    def get_queryset(self):
        return User.objects.filter(**self.request.GET.dict())


class UserAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DjangoUserSerializer


#                                Client

class ClientAPIView(ListCreateAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.filter(**self.request.GET.dict())


class ClientAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ClientSerializer


#                                Foods

class FoodsAPIView(ListCreateAPIView):
    serializer_class = FoodsSerializer

    def get_queryset(self):
        return Food.objects.filter(**self.request.GET.dict())


class FoodsAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodsSerializer


#                                Table

class TableAPIView(ListCreateAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Table.objects.filter(**self.request.GET.dict())


class TableAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


#                                TableOrder

class TableOrderAPIView(ListCreateAPIView):
    serializer_class = TableOrderSerializer

    def get_queryset(self):
        return TableOrder.objects.filter(**self.request.GET.dict())


class TableOrderAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = TableOrder.objects.all()
    serializer_class = TableOrderSerializer


#                                OrderFood

class OrderFoodAPIView(ListCreateAPIView):
    serializer_class = OrderFoodSerializer

    def get_queryset(self):
        return OrderFood.objects.filter(**self.request.GET.dict())


class OrderFoodAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = OrderFood.objects.all()
    serializer_class = OrderFoodSerializer


#                                Reating

class RatingAPIView(ListCreateAPIView):  # ((total*count) + new_total) / count
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(**self.request.GET.dict())

    def perform_create(self, serializer):
        request = serializer.context['request']
        return serializer.save(client=Client.objects.get(user=request.user))

    def post(self, request, *args, **kwargs):
        client = Client.objects.get(user=request.user).id
        food = request.data['food']
        count = Rating.objects.all().count()
        try:
            rating = Rating.objects.get(client=client, food=food)
            if rating:
                rating.rating = request.data['rating']
                rating.save()

                ##################

                rating = Rating.objects.values_list('rating', flat=True)
                count = Rating.objects.all().count()
                total = sum(rating)
                new_rating = total / count
                food = Food.objects.get(id=food)
                food.rate = new_rating
                food.save()

                ##################     

                return Response(status=200)
        except:

            ##################
            rating = Rating.objects.values_list('rating', flat=True)
            count = Rating.objects.all().count()

            total = sum(rating)
            new_rating = total / count
            food = Food.objects.get(id=food)
            food.rate = new_rating
            food.save()
            ##################
            return super().post(request, *args, **kwargs)


class RatingAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
