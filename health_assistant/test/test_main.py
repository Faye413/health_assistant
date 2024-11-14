import unittest
from health_assistant.main import create_health_schedule_with_rag

class TestMain(unittest.TestCase):
    def test_create_health_schedule(self):
        user_data = {
            'sleep_quality': [6.5, 7, 8, 6, 7.5],
            'steps': [10000, 12000, 9500, 11000, 12500],
            'heart_rate': [65, 70, 68, 72, 69]
        }
        user_query = "Create a wellness plan for better sleep."
        response = create_health_schedule_with_rag(user_data, user_query)
        self.assertIsNotNone(response)
