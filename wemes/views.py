from rest_framework import permissions, viewsets

from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAdminUser]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAdminUser]

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class =ColorSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

# class QRCodeViewSet(viewsets.ModelViewSet):
#     queryset = QRCode.objects.all()
#     serializer_class = QRCodeSerializer
#     permission_classes = [permissions.IsAdminUser]