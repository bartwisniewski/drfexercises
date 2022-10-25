from typing import List
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from API.serializers import ValveSerializer, PumpSerializer, BookSerializer
from books.models import Book, Author
from processautomation.models import Valve, Pump
from books.data_provider import get_books_data, QUERY_KEY, ALLOWED_VALUES


def clear_string_list(string_list: List[str]) -> None:
    cleaning_functions = [clear_quotation_mark]
    n = 0
    for element in string_list:
        for cleaning_function in cleaning_functions:
            string_list[n] = cleaning_function(string_list[n])
        n += 1


def clear_quotation_mark(text: str) -> str:
    quotations = ['"', "'"]
    if text[0] in quotations:
        text = text[1:]
    if text[-1] in quotations:
        text = text[:-1]
    return text


class BooksListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    ALLOWED_SORTS = ['published_date', '-published_date']

    def get_queryset(self):
        queryset = Book.objects.all()
        published_date_filter = self.request.query_params.get('published_date')
        authors_filter = self.request.query_params.getlist('author')
        sort = self.request.query_params.get('sort')
        if published_date_filter is not None:
            queryset = queryset.filter(published_date=published_date_filter)
        if authors_filter:
            clear_string_list(authors_filter)
            queryset = queryset.filter(authors__name__in=authors_filter)
        if sort in BooksListView.ALLOWED_SORTS:
            queryset = queryset.order_by(sort)
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class DbFillView(APIView):
    http_method_names = ["post"]

    def post(self, request):
        set_name = request.data.get(QUERY_KEY)
        if set_name in ALLOWED_VALUES:
            data = get_books_data(set_name)
            response = Response({}, status=status.HTTP_200_OK)
        else:
            response = Response({}, status=status.HTTP_403_FORBIDDEN)
        return response


class ValvesListCreate(generics.ListCreateAPIView):
    serializer_class = ValveSerializer
    queryset = Valve.objects.all()


class ValvesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ValveSerializer
    queryset = Valve.objects.all()


class PumpsListCreate(generics.ListCreateAPIView):
    serializer_class = PumpSerializer
    queryset = Pump.objects.all()


class PumpsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PumpSerializer
    queryset = Pump.objects.all()
