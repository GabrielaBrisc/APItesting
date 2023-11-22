from api_tests.app_requests.api_client import *
from api_tests.app_requests.order import *

class TestOrders:

    #inainte de fiecare test facem un create account, apoi ne folosim de acel token pentru a putea face o comanda
    def setup_method(self):
        self.token = get_token()

    #### ????
    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, 'Gabi')
        assert response.status_code == 404 , "Status code is not correct"
        assert response.json()['error'] == "This book is not in stock. Try again later."

    def test_add_valid_order(self):
        response =add_order(self.token,1,"Gabi")
        assert response.status_code == 201
        assert response.json()['created'] is True
        #clean_up
        delete_order(self.token,response.json()['orderId'])

    def test_get_invalid_order_id(self):
        response = get_order(self.token, "345435")
        assert response.status_code ==404
        assert response.json()['error'] == "No order with id 345435."

    #Update an existing order. Requires authentication.
    # The request body needs to be in JSON format and allows you to update the following properties:
    # customerName - String
    def test_patch_invalid_order_id(self):
        response = get_order(self.token,"15445")
        assert response.status_code == 404
        assert response.json()['error'] == "No order with id 15445"

    #patch https://simple-books-api.glitch.me/orders/uSl5sx1HnPl7z9Z0U_k1H
    def test_patch_valid_order_id(self):
        #prima data adaugam comanda ca sa stim id ul ei cand dorim sa o modificam
        order_id = add_order(self.token,1,"Gabi").json()['orderId']
        #modificam customer name in Gabi2 din Gabi
        response = edit_order(self.token,order_id,"Gabi2")
        assert response.status_code == 204
        #verificam si continutul ca s a schimbat iar pentru aceasta am apelat get order
        #deoarece cand am modificat comanda am avut doar status codul ca e ok,
        # dar nu am putut vedea ca si continutul s a modificat
        get = get_order(self.token, order_id)
        assert get.json()['customerName'] == "Gabi2"

        delete_order(self.token, order_id)

        #delete https://simple-books-api.glitch.me/orders/uSl5sx1HnPl7z9Z0U_k1H
    def test_delete_order(self):
        #intai adaug o comanda
        add = add_order(self.token, 1, 'user1')
        #ne am asigurat ca comanda e stearsa
        response = delete_order(self.token, add.json()['orderId'])
        assert response.status_code == 204
        #verific daca atunci cand dau get orders, nu mai avem nimic
        #verificam lungimea sa fie 0, adica nu avem nicio comanda
        get_all =get_orders(self.token)
        assert len(get_all.json) ==0

    def test_delete_invalid_order_id(self):
        response = delete_order(self.token, "asmgewgfew")
        assert response.status_code ==404
        assert  response.json()['error'] =="No order with id asmgewgfew."