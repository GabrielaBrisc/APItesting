from api_tests.app_requests.api_client import *

class TestAPIClient:

    #cream cu (metoda) randint un nr din acel interva; care sa fie inclus in email
    # la fiecare rulare facuta o sa mi se genereze alt email
    nr = randint(1,9999)
    clientName = "Gabi"
    clientEmail = f'valid_email_test{nr}@mail.com'

    def setup_method(self):
        self.response = login(self.clientName, self.clientEmail)

        #noi stim doar ca, apeland acel api o sa ni se dea o cheie (accessToken) si un response pe care nu il stim de dinainte
        #aceasta cheie se genereaza pt fiecare email

    def test_successful_login(self):
        assert self.response.status_code == 201, "Actual status code is not correct" #de ce e incorect
        #noi o sa verificam daca exista in cheia care apare in raspuns acest accessToken
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in response'

    #verificam daca acel cont a fost deja creat
    def test_login_client_already_registered(self):
        self.response = login(self.clientName,self.clientEmail)
        assert self.response.status_code == 409
        assert self.response.json()['error'] == 'API client already registered. Try a different email.'

    #verificam cu email invalid
    def test_invalid_email(self):
        self.response = login('def', 'abc')
        assert self.response.status_code == 400
        assert self.response.json()['error'] == "Invalid or missing client email."

