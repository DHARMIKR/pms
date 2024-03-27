import requests
import unittest

class LoginTest(unittest.TestCase):
    def make_login_request(self, username=None, password=None):
        url = "http://127.0.0.1:5000/api/login"
        headers = {"Content-Type": "application/json"}
        data = {"username": username, "password": password}
        s = requests.Session()
        return s.post(url, json=data, headers=headers, verify=False)

    def test_login_successful(self):
        response = self.make_login_request(username="sample", password="Hello@12345678")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "Login Successful")

    def test_wrong_username(self):
        response = self.make_login_request(username="wrong_username", password="Hello@12345678")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "Login Failed")

    def test_wrong_password(self):
        response = self.make_login_request(username="sample", password="wrong_password")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "Login Failed")

    def test_no_username_field(self):
        response = self.make_login_request(password="Hello@12345678")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "Login Failed")

    def test_no_password_field(self):
        response = self.make_login_request(username="sample")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "Login Failed")

if __name__ == "__main__":
    unittest.main()
