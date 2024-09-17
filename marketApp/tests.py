from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from marketApp.models import Category, Subcategory, Product, CartView
from usersApp.models import User


class MarketAppTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@mail.ru')
        self.client.force_authenticate(self.user)
        self.category1 = Category.objects.create(name='тест-категория')
        self.subcategory1 = Subcategory.objects.create(name='тест-подкатегория', associated_category=self.category1)
        self.product1 = Product.objects.create(name='тест-продукт', price=33, associated_subcategory=self.subcategory1)
        self.product2 = Product.objects.create(name='тест-продукт2', price=54, associated_subcategory=self.subcategory1)
        self.cartview = CartView.objects.create(product_id=self.product1.pk, quantity=2, owner=self.user)

    def test_category_create(self):
        data = {
            "name": "тест2"
        }
        url = reverse('marketApp:category-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["name"], 'тест2')

    def test_category_list(self):
        url = reverse('marketApp:category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['name'], 'тест-категория')
        self.assertEqual(response.json()['results'][0]['slug'], 'test-kategorija')

    def test_category_update(self):
        data = {
            "name": 'update'
        }
        url = reverse('marketApp:category-update', args=(self.category1.pk,))
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'update')

    def test_category_destroy(self):
        url = reverse('marketApp:category-destroy', args=(self.category1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = reverse('marketApp:category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.json()['results']), 0)

    def test_subcategory_create(self):
        data = {
            "name": "продукт",
            "associated_category": self.category1.pk
        }
        url = reverse('marketApp:subcategory-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'продукт')

    def test_subcategory_list(self):
        url = reverse('marketApp:subcategory-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['name'], 'тест-подкатегория')
        self.assertEqual(response.json()['results'][0]['slug'], 'test-podkategorija')

    def test_subcategory_update(self):
        data = {
            "name": "update",
            "associated_category": self.category1.pk
        }
        url = reverse('marketApp:subcategory-update', args=(self.subcategory1.pk,))
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'update')

        url = reverse('marketApp:subcategory-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['results'][0]['slug'], 'update')

    def test_subcategory_destroy(self):
        url = reverse('marketApp:subcategory-destroy', args=(self.subcategory1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = reverse('marketApp:subcategory-list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.json()['results']), 0)

    def test_product_create(self):
        data = {
            "name": "продукт",
            "price": 35,
            "associated_subcategory": self.subcategory1.pk
        }
        url = reverse('marketApp:product-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'продукт')

    def test_product_list(self):
        url = reverse('marketApp:product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['name'], 'тест-продукт')
        self.assertEqual(response.json()['results'][0]['slug'], 'test-produkt')
        self.assertEqual(response.json()['results'][0]['price'], 33)

    def test_product_retrieve(self):
        url = reverse('marketApp:product-retrieve', args=(self.product2.pk,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'тест-продукт2')
        self.assertEqual(response.json()['slug'], 'test-produkt2')
        self.assertEqual(response.json()['price'], 54)

    def test_product_update(self):
        data = {
            "name": "update",
            "price": 77,
            "associated_subcategory": self.subcategory1.pk
        }
        url = reverse('marketApp:product-update', args=(self.product1.pk,))
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'update')
        self.assertEqual(response.json()['price'], 77)

        url = reverse('marketApp:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['slug'], 'update')

    def test_product_destroy(self):
        url = reverse('marketApp:product-destroy', args=(self.product1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = reverse('marketApp:product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.json()['results']), 1)

    def test_cart_view_create(self):
        data = {
            "product_id": self.product2.pk,
            "quantity": 1
        }
        url = reverse('marketApp:cart-view-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('marketApp:cart-view-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['items'][1]['quantity'], 1)
        self.assertEqual(len(response.json()['items']), 2)

        data = {
            "product_id": self.product2.pk,
            "quantity": 1
        }
        url = reverse('marketApp:cart-view-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('marketApp:cart-view-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['items'][1]['quantity'], 2)
        self.assertEqual(len(response.json()['items']), 2)

    def test_cart_view_list(self):
        url = reverse('marketApp:cart-view-list')
        response = self.client.get(url, format='json')
        data = {'items': [
            {
                'id': self.cartview.pk,
                'quantity': self.cartview.quantity,
                'owner': self.user.pk,
                'product': self.product1.pk
            }
        ],
            'total_quantity': 2,
            'total_price': 66
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

    def test_cart_view_destroy(self):
        url = reverse('marketApp:cart-view-destroy', args=(self.product1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = reverse('marketApp:cart-view-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['items'][0]['quantity'], 1)

        url = reverse('marketApp:cart-view-destroy', args=(self.product1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = reverse('marketApp:cart-view-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['items'], [])

    def test_cart_view_all_destroy(self):
        url = reverse('marketApp:cart-view-list')
        response = self.client.get(url, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()['items'],
            [
                {
                    'id': self.cartview.pk,
                    'quantity': self.cartview.quantity,
                    'owner': self.user.pk,
                    'product': self.product1.pk
                }
            ]
        )

        url = reverse('marketApp:cart-view-all-destroy')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = reverse('marketApp:cart-view-list')
        response = self.client.get(url, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['items'], [])
