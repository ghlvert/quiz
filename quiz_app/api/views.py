from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets

from quiz_app.api.serializers import FullQuizSerializer, QuizSerializer
from quiz_app.models import Quiz

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = FullQuizSerializer

    def list(self, request, *args, **kwargs):
        queryset = Quiz.objects.all()
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)