from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class NumberSet:
    def __init__(self):
        self.numbers = set(range(1, 101))

    def extract(self, number):
        if number < 1 or number > 100:
            raise ValueError("Número fuera de rango")
        self.numbers.remove(number)

    def find_missing(self):
        return (set(range(1, 101)) - self.numbers).pop()


class MissingNumberView(APIView):
    def post(self, request):
        number = int(request.data.get('number'))
        if not (1 <= number <= 100):
            return Response({'error': 'Número inválido'}, status=400)

        numbers = NumberSet()
        numbers.extract(number)
        missing_number = numbers.find_missing()
        return Response({'missing_number': missing_number})
