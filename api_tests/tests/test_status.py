from api_tests.app_requests.status import *

class TestStatus():

    # https://simple-books-api.glitch.me/status
    def test_status_code(self):
        response = get_status()
        print(response.status_code)
        assert response.status_code == 200, f"expected code is 200, but was {response.status_code}"

    # body response {
    #     "status": "OK"
    # }
    # https://simple-books-api.glitch.me/status
    def test_status_body(self):
        response = get_status()
        print(response.json())
        assert response.json()["status"] == "OK", f" expected value was OK, but actually it was {response.json(['status'])}"
