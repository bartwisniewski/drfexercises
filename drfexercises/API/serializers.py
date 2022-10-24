from processautomation.models import Valve, Pump
from books.models import Book, Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class ValveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Valve
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'api-valve', 'lookup_field': 'pk'},
        }


class PumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pump
        fields = '__all__'
