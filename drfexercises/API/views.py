from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from API.serializers import ValveSerializer, PumpSerializer
from processautomation.models import Valve, Pump
from books.data_provider import get_books_data, QUERY_KEY, ALLOWED_VALUES


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
