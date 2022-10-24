import requests
import json
from rest_framework import status
from books.models import Book, Author

DATA_SOURCE = 'https://www.googleapis.com/books/v1/volumes'
QUERY_KEY = 'q'
ALLOWED_VALUES = ['war', 'Hobbit']


def get_books_data(set_name: str) -> dict:
    url = f'{DATA_SOURCE}?{QUERY_KEY}={set_name}'
    response = requests.get(url)
    data = {}
    if response.status_code == status.HTTP_200_OK:
        try:
            data = response.json()
            google_data_to_django(data)
        except requests.exceptions.JSONDecodeError:
            pass
    return data


def google_data_to_django(data: dict) -> None:
    print("google data to django")
    it = 1
    for book in data.get('items'):
        print(f"book number {it}")
        print(book)
        it += 1
        volume_info = book.get('volumeInfo')
        defaults = {'etag': book.get('etag'),
                    'title': volume_info.get('title'),
                    'published_date': volume_info.get('publishedDate'),
                    'categories': json.dumps(volume_info.get('categories')),
                    'average_rating': volume_info.get('average_rating'),
                    'ratings_count': volume_info.get('ratings_count'),
                    }

        if 'imageLinks' in list(volume_info.keys()):
            defaults['thumbnail'] = volume_info['imageLinks'].get('thumbnail')

        new_book, created = Book.objects.update_or_create(book_id=book.get('id'), defaults=defaults)

        authors = volume_info.get('authors')
        if authors:
            for author in authors:
                a, created = Author.objects.get_or_create(name=author)
                new_book.authors.add(a)

        new_book.save()
