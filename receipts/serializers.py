from rest_framework import serializers
from .models import Receipt, ReceiptFile


class ReceiptListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = "__all__"


class ReceiptFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptFile
        fields = "__all__"


class ReceiptSerializer(serializers.ModelSerializer):
    files = ReceiptFileSerializer(many=True, read_only=True)

    class Meta:
        model = Receipt
        fields = ['amount', 'name', 'address', 'phone_number', 'files', 'description']
