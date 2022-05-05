from django.test import TestCase
import logging

logger = logging.getLogger(__name__)


class BaseNotificationsTests(TestCase):

    def test_index_loads(self):
        """Проверяет доступность страницы"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
