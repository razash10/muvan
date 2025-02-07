import unittest
from app import muvan

class PropertiesOfLeasesAboutToExpireTestCase(unittest.TestCase):
    def setUp(self):
        self.app = muvan.create_app().test_client()
        self.app.testing = True

    def test_properties_of_leases_about_to_expire_zero_days(self):
        response = self.app.get('/properties_of_leases_about_to_expire/0')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("properties", data)
        self.assertIsInstance(data["properties"], list)
        self.assertEqual(data["properties"], [])

    def test_properties_of_leases_about_to_expire_thirty_days(self):
        response = self.app.get('/properties_of_leases_about_to_expire/30')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("properties", data)
        self.assertIsInstance(data["properties"], list)
        self.assertEqual(data["properties"], [3, 5, 6])

    def test_properties_of_leases_about_to_expire_ninety_days(self):
        response = self.app.get('/properties_of_leases_about_to_expire/90')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("properties", data)
        self.assertIsInstance(data["properties"], list)
        self.assertEqual(data["properties"], [3, 4, 5, 6, 8])
