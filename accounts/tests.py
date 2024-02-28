from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import Account
from consumers.models import Consumer

TEST_DATA = [
    {
        'balance': 500.45,
        'client_reference_no': '448f5f0f-f1b3-4062-9d0e-3b07aa2ec99c',
        'status': 'PAID_IN_FULL'
    },
    {
        'balance': 200.45,
        'client_reference_no': '448f5f0f-f1b3-4062-9d0e-3b07aa2ec99c',
        'status': 'PAID_IN_FULL'
    },
    {
        'balance': 100.45,
        'client_reference_no': '448f5f0f-f1b3-4062-9d0e-3b07aa2ec99c',
        'status': 'IN_COLLECTION'
    },
    {
        'balance': 60.45,
        'client_reference_no': '448f5f0f-f1b3-4062-9d0e-3b07aa2ec99c',
        'status': 'INACTIVE'
    },
    {
        'balance': 50.00,
        'client_reference_no': '448f5f0f-f1b3-4062-9d0e-3b07aa2ec99c',
        'status': 'INACTIVE'
    },
]

class TestAccountsAPITestCase(APITestCase):

    def setUp(self):
        consumer = Consumer.objects.create(name='David Chinchin', address='Quito - Ecuador', ssn='123-234-233')
        for data in TEST_DATA:
            Account.objects.create(**data, consumer=consumer)

    def test_get_all_records(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], len(TEST_DATA))

    def test_get_max_balance(self):
        """
        shuld be return 3 rows
        """
        response = self.client.get('/accounts/?max_balance=100.45')
        self.assertEqual(response.data['count'], 3)

    def test_get_min_balance(self):
        """
        shuld be return 2 rows
        """
        response = self.client.get('/accounts/?min_balance=200.45')
        self.assertEqual(response.data['count'], 2)

    def test_min_and_max_balance(self):
        """
        shuld be return 3 rows
        """
        response = self.client.get('/accounts/?min_balance=60.45&max_balance=200.45')
        self.assertEqual(response.data['count'], 3)

    def test_get_by_consumer_name_exists(self):
        """
        shuld be return 3 rows
        """
        response = self.client.get('/accounts/?consumer_name=David Chinchin')
        self.assertGreater(response.data['count'], 0)
    
    def test_get_by_consumer_name_not_exists(self):
        """
        shuld be return 3 rows
        """
        response = self.client.get('/accounts/?consumer_name=Pedro')
        self.assertEqual(response.data['count'], 0)
