from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'receipts', views.GetReceiptsViewSet, basename='receipts')

urlpatterns = [
    path('user/', views.ListCreateUserReceipts.as_view(), name="create_and_list_user_receipts")
] + router.urls

print(urlpatterns)



