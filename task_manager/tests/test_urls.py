from django.test import TestCase
from django.urls import reverse

class URLTests(TestCase):
    def test_index_view(self):
        # Проверка доступности главной страницы
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        # Проверка доступности страницы входа
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        # Проверка поведения при выходе (ожидается редирект)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
