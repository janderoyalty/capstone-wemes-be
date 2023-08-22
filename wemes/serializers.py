from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()  # Use SerializerMethodField

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_num', 'last_four', 'email', 'admin', 'is_active', 'transactions']

    def get_transactions(self, user):  # Custom method to get transactions
        transactions = Transaction.objects.filter(customer=user)  # Adjust the filter condition based on your model relationships
        transaction_serializer = TransactionSerializer(transactions, many=True)
        return transaction_serializer.data
    
class TransactionSerializer(serializers.ModelSerializer):
    # parent_lookup_kwargs = {
    #     'user': 'user',
    # }
    # admin = UserSerializer()
    # customer = UserSerializer()

    # admin_name = serializers.CharField(read_only=True, source="admin.name")
    # customer_name = serializers.CharField(read_only=True, source="customer.name")

    class Meta:
        model = Transaction
        fields = ['id', 'drop_off', "admin", "customer", 'items', "description"]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    # parent_lookup_kwargs = {
    # 'item': 'item_h',
    # 'user': 'item_h__user',
    # }
    # color = ColorSerializer()
    # category = CategorySerializer()
    

    class Meta:
        model = Item
        fields = ['id', 'drop_off', 'due_date', 'transaction', 'category', 'color', "is_shoe", "follow_up", "description", "tag_id"]


# class QRCodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QRCode
#         fields = ['id', 'number', 'code']