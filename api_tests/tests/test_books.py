from api_tests.app_requests.books import *

class TestBooks():

    #postman: get https://simple-books-api.glitch.me/status
    def test_status_code(self):
        response = get_books()
    # de unde vine acest status.code?
        assert response.status_code == 200, "Status code should be 200"

    #postman: get https://simple-books-api.glitch.me/books?type=adventure
    def test_get_books_invalid_type(self):
        response = get_books(book_type="adventure")
        assert response.status_code == 400, "Status code should be 400"
        assert response.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    #postman: get https://simple-books-api.glitch.me/books?
    def test_get_all_books(self):
        response = get_books()
        #avem o lista cu 6 elemente

        assert len(response.json()) == 6, "Total number of books should be 6"
        for book in response.json():
            #fiecare element contine urmatoarele campuri (atribute):
            assert 'id' in book.keys()
            assert "available" in book.keys()
            assert "name" in book.keys()
            assert "type" in book.keys()

    # https://simple-books-api.glitch.me/books?type=&limit=
    def test_get_all_books_limit(self):
        response = get_books(limit=4)
        #verific daca nr de elemente este 4
        assert len(response.json()) == 4, "Total number of books should be 3"
        #verificam daca sunt in ordine
        i=1
        for book in response.json():
            assert book['id'] == i
            i+=1

    def test_get_all_books_type_fiction(self):
        response = get_books(book_type='fiction')
        for book in response.json():
            assert book['type'] == 'fiction', "Book type should be fiction"

    #de verif si daca pun la limita 1. nu ar trebui prima data sa verif daca cartile sunt fiction si dupa sa verific limita?
    def test_get_all_books_type_and_limit(self):
        response = get_books(book_type='fiction', limit=2)
        #verific daca am doar 2 elemente
        assert len(response.json()) == 2, "Number of books returned should be 2"
        for book in response.json():
            #verific daca sunt de tipul fiction
            assert book['type'] == 'fiction', 'Book type should be fiction'

    #Get a single book: GET /books/:bookId
    #Retrieve detailed information about a book.
    # get https://simple-books-api.glitch.me/books/4
    def test_get_book(self):
        response = get_book(4)
        assert response.status_code == 200, 'Status code should be 200'
        assert response.json()['id'] == 4 ,"Id should be 4"

    # get https://simple-books-api.glitch.me/books/9
    def test_get_wrong_id(self):
        response = get_book(9)
        assert response.status_code == 404, 'Status code should be 404'
        #verific sa existe cheia de error
        assert 'error' in response.json().keys()
        #verific mesajul, raspunsul
        assert response.json()['error'] == "No book with id 9"