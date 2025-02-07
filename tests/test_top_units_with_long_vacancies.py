import unittest
from app import muvan

class TopUnitsWithLongVacanciesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = muvan.create_app().test_client()
        self.app.testing = True

    def test_top_zero_units_with_long_vacancies(self):
        response = self.app.get('/top_units_with_long_vacancies/0')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("units", data)
        self.assertIsInstance(data["units"], list)
        self.assertEqual(data["units"], [])

    def test_top_three_units_with_long_vacancies(self):
        response = self.app.get('/top_units_with_long_vacancies/3')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("units", data)
        self.assertIsInstance(data["units"], list)
        self.assertEqual(data["units"], [39, 19, 37])

    def test_top_five_units_with_long_vacancies(self):
        response = self.app.get('/top_units_with_long_vacancies/5')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("units", data)
        self.assertIsInstance(data["units"], list)
        self.assertEqual(data["units"], [39, 19, 37, 72, 89])
