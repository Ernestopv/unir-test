import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # en segundos

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def get_response(self, url):
        """Metodo de ayuda para obtener la respuesta API"""
        return urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_api_add_success(self):
        url = f"{BASE_URL}/calc/add/2/3"
        response = self.get_response(url)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "5")

    def test_api_add_invalid_params(self):
        url = f"{BASE_URL}/calc/add/a/b"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_subtract_success(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = self.get_response(url)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2")

    def test_api_subtract_invalid_params(self):
        url = f"{BASE_URL}/calc/substract/x/y"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_multiply_success(self):
        url = f"{BASE_URL}/calc/multiply/4/2"
        response = self.get_response(url)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "8")

    def test_api_multiply_invalid_params(self):
        url = f"{BASE_URL}/calc/multiply/a/b"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_divide_success(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = self.get_response(url)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "5.0")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
        self.assertIn("Division by zero", e.exception.read().decode())

    def test_api_divide_invalid_params(self):
        url = f"{BASE_URL}/calc/divide/a/b"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_power_success(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = self.get_response(url)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "8")

    def test_api_power_invalid_params(self):
        url = f"{BASE_URL}/calc/power/a/b"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_square_root_success(self):
        url = f"{BASE_URL}/calc/square_root/16"
        response = self.get_response(url)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "4.0")

    def test_api_square_root_negative(self):
        url = f"{BASE_URL}/calc/square_root/-16"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
        self.assertIn("Cannot calculate square root of a negative number", e.exception.read().decode())

    def test_api_square_root_invalid_params(self):
        url = f"{BASE_URL}/calc/square_root/a"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)

    def test_api_log_base_10_success(self):
        url = f"{BASE_URL}/calc/log_base_10/100"
        response = self.get_response(url)
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(response.read().decode(), "2.0")

    def test_api_log_base_10_zero(self):
        url = f"{BASE_URL}/calc/log_base_10/0"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
        self.assertIn("Logarithm is only defined for positive numbers", e.exception.read().decode())

    def test_api_log_base_10_negative(self):
        url = f"{BASE_URL}/calc/log_base_10/-10"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
        self.assertIn("Logarithm is only defined for positive numbers", e.exception.read().decode())

    def test_api_log_base_10_invalid_params(self):
        url = f"{BASE_URL}/calc/log_base_10/a"
        with self.assertRaises(HTTPError) as e:
            self.get_response(url)
        self.assertEqual(e.exception.code, http.client.BAD_REQUEST)
