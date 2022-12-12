from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import PerevalAdded
from .serializers import PerevalAddedSerializer, PerevalReadSerializer


class PerevalView(viewsets.ViewSet):

    @staticmethod
    def submit_data(request):
        id = None
        message = None
        try:
            serialaizer = PerevalAddedSerializer(data=request.data)
            if serialaizer.is_valid():
                ser = serialaizer.save()
                id = ser.id
                status = 200
            else:
                message = f'Bad request: {serialaizer.errors}'
                status = 400
        except BaseException as e:
            status = 500
            message = f'Ошибка сервера: {e.data}'
        finally:
            return Response({"status": f"{status}", "message": f"{message}", "id": f"{id}"})

    @staticmethod
    def list_for_user(request):
        if 'user__email' in request.GET:
            queryset = PerevalAdded.objects.filter(user__email=request.GET['user__email'])
            serializer = PerevalReadSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response('Empty response')

    @staticmethod
    def get_record(request, pk):
        queryset = PerevalAdded.objects.all()
        pereval = get_object_or_404(queryset, pk=pk)
        serializer = PerevalReadSerializer(pereval)
        return Response(serializer.data)

    @staticmethod
    def update_record(request, pk):
        try:
            pereval = PerevalAdded.objects.get(pk=pk)
        except:
            return Response({"state": "0", "message": "Object does not exists"})
        serializer = PerevalAddedSerializer(data=request.data, instance=pereval)
        if serializer.is_valid():
            serializer.save()
            return Response({"state": "1"})
        else:
            return Response({"state": "0", "message": "Bad request"})

