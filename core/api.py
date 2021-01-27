from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from .serializers import MealSerializer
from .models import Meal


class MealModelViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permissions_classes = [permissions.AllowAny]