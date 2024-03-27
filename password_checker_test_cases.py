import unittest
import requests

class PasswordCheckerTest(unittest.TestCase):
    def make_password_checker_request(self, password=None):
        url = "http://127.0.0.1:5000/api/secure_password_checker"
        headers = {"Content-Type": "application/json"}
        data = {"password": password}
        s = requests.Session()
        return s.post(url, json=data, headers=headers, verify=False)

    def test_breached_password(self):
        response = self.make_password_checker_request(password="password123")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "You're password is breached before.")

    def test_secure_password(self):
        response = self.make_password_checker_request(password="Hello@12345678999")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertNotEqual(response.json()["message"], "You're password is breached before.")

if __name__ == "__main__":
    unittest.main()
