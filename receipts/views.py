from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from .models import Receipt
from .serializers import ReceiptSerializer, ReceiptFileSerializer, ReceiptListSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.


class GetReceiptsViewSet(viewsets.ViewSet):

    def list(self, request):
        query_set = Receipt.objects.all()
        serializer = ReceiptSerializer(instance=query_set, many=True)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        try:
            receipt = Receipt.objects.get(pk=pk)
        except Receipt.DoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "data": 'Receipt Doed not exist'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = ReceiptSerializer(receipt)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data}, status=status.HTTP_200_OK)


class ListCreateUserReceipts(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ReceiptSerializer

    def get(self, request):
        query_set = Receipt.objects.filter(user=request.user)
        serializer = ReceiptListSerializer(instance=query_set, many=True)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ReceiptSerializer)
    def post(self, request):
        serializer = ReceiptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({"status": status.HTTP_201_CREATED, "data": serializer.data},
                        status=status.HTTP_201_CREATED)
