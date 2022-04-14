from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from users.models import User
from .models import ReceiptFile


# Create your tests here.
class ReceiptsTest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='TestUser', password='qwertyuiop')
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_receipt_create(self):
        """
        Ensure we can create a receipt and the 10 files are generated for it.
        """
        url = reverse('create_and_list_user_receipts')
        data = {'name': 'Test User', 'amount': 300.00, 'address': 'Test Address', 'phone_number': '080123456789',
                'description': 'Test Description'}
        response = self.client.post(url, data)
        files = ReceiptFile.objects.count()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(10, files)

    def test_user_receipt_list(self):
        """
        Ensure the request to get list of users receipts works correctly
        """
        url = reverse('create_and_list_user_receipts')
        response = self.client.get(url)
        length = len(response.json().get('data'))
        self.assertEqual(response.status_code, 200)



