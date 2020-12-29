from django.db.models import manager
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_200_OK
from .serializers import StockSerializer
from .models import Stock

# Create your views here.
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        ans = {
            "msg": "Test"
        }
        return Response(ans)

class StockPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 500

class StockView(APIView):
    
    def get(self, request, *args, **kwargs):
        if request.GET.get('ticker'):
            qs = Stock.objects.filter(ticker=request.GET.get('ticker'))
            serializer = StockSerializer(qs, many=True)
            return Response(serializer.data)
        else:
            qs = Stock.objects.all()
            paginator = StockPagination()
            result_page = paginator.paginate_queryset(qs, request)
            serializer = StockSerializer(result_page, many=True, context={'request': request})
            return Response(serializer.data, status=HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)