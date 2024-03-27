import requests
import unittest

class SignupTest(unittest.TestCase):
    def make_signup_request(self, username=None, password=None):
        url = "http://127.0.0.1:5000/api/user_creation"
        headers = {"Content-Type": "application/json"}
        data = {"username": username, "password": password}
        s = requests.Session()
        response = s.post(url, json=data, headers=headers, verify=False)
        return response

    def test_successful_signup(self):
        response = self.make_signup_request(username="sample5", password="Hello@12345678999")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "User has been created.")

    def test_user_exist(self):
        response = self.make_signup_request(username="sample3", password="Hello@12345678999")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "User already exist.")

    def test_weak_password_signup(self):
        response = self.make_signup_request(username="sample", password="Hello@1234567")
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertEqual(response.json()["message"], "You're password is breached before.")

if __name__ == "__main__":
    unittest.main()
