from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Receipt


# Create your tests here.
class ReceiptsTest(APITestCase):

    def setUp(self) -> None:

    def test_receipt_create(self):
        """
        Ensure we can create a receipt and the 10 files are generated for it.
        """
        url = reverse('create_and_list_user_receipt')
        data = {'name': 'Test User', 'amount': 300.00, }
