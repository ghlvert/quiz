from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from quiz_app.forms import FormFactory
from quiz_app.models import Question, Variant, Quiz
from formtools.wizard.views import SessionWizardView
from django.views.decorators.http import require_POST

from quiz_app.quiz_collection import QuizCollection
# Create your views here.

def index(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz_app/index.html', {'quizes': quizes})


def quiz_detail(request, quiz_id=1):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    form_num = int(request.GET.get("num", 1))
    questions = quiz.questions.all()
    if form_num > questions.count():
        collection = QuizCollection(request)
        right_answers = collection.count(quiz.id)
        collection.clear(quiz.id)
        return HttpResponse(right_answers)
    else:
        formset = FormFactory(instance=questions[form_num-1])
        for form in formset.forms:
            if form.initial['id']:
                form.initial['checked'] = False
    return render(request, 'quiz_app/detail_quiz.html', {'quiz': quiz, 'formset': formset,
                                                          'question': questions[form_num-1], 'form_num':form_num})

@require_POST
def question_processing(request, quiz_id=1, question_id=1):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    curr_question = questions[question_id-1]
    formset = FormFactory(request.POST, instance=curr_question)
    right = True
    if formset.is_valid():
        for form in formset.forms:
            if not (form.cleaned_data['checked'] == form.initial['checked']):
                right = False
                break
                
    if right:
        collection = QuizCollection(request)
        collection.add_point(quiz.id, curr_question.id)
        print(collection.count(quiz.id))
        print(collection.collection)
    base_url = reverse("quiz_detail", args=(quiz.id,))
    url = f'{base_url}?num={question_id+1}'
    return redirect(url)

