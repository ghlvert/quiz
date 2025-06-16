from dataclasses import field
from rest_framework import serializers

from quiz_app.models import Question, Quiz, Variant

class VariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['text', 'checked']

class QuestionSerializer(serializers.ModelSerializer):
    variants = VariantsSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['title', 'descripiton', 'variants']

class FullQuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['title', 'descripiton', 'questions']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['title', 'descripiton']


