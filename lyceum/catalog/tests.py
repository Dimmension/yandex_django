from django.test import Client, TestCase
from parameterized import parameterized


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client.get("/catalog/")
        self.assertEqual(response.status_code, 200)

    @parameterized.expand(
        [
            ("negative", [-i for i in range(1, 101)], 404),
            ("positive", [i for i in range(101)], 200),
        ]
    )
    def test_catalog_pk_endpoint(self, name, a, b):
        for i in range(100):
            self.assertEqual(Client().get(f"/catalog/{a[i]}").status_code, b)
