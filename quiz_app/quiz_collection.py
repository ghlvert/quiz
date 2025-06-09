# class QuizCollection:
#     def __init__(self, request):
#         self.request = request
#         collection = self.request.session.get('collection')
#         if not collection:
#             request.session['collection'] = {}
#             collection = request.session['collection']
#         self.collection = collection

#     def add_point(self, quiz_id, question_id):
#         quiz_id = str(quiz_id)
#         question_id = str(question_id)
#         if not self.collection.get(quiz_id):
#             self.collection[quiz_id] = {}
#         self.collection[quiz_id][question_id] = 1
#         self.save()

#     def clear(self, quiz_id):
#         if self.collection.get(str(quiz_id)):
#             del self.collection[str(quiz_id)]
#             self.save()

#     def count(self, quiz_id):
#         try:
#             return len(self.collection[str(quiz_id)])
#         except:
#             return 0

#     def save(self):
#         self.request.session.modified = True

from quiz_app.models import Quiz, Question
from copy import deepcopy

class QuizCollection:
    def __init__(self, request):
        self.request = request
        collection = self.request.session.get('collection')
        if not collection:
            request.session['collection'] = {}
            collection = request.session['collection']
        self.collection = collection

    def add_point(self, quiz_id, question_id):
        quiz_id = str(quiz_id)
        question_id = str(question_id)
        if not self.collection.get(quiz_id):
            self.collection[quiz_id] = {}
        self.collection[quiz_id][question_id] = 1
        self.save()
    
    def add_results(self, quiz_id, question_id, formset):
        quiz_id = str(quiz_id)
        question_id = str(question_id)
        if not self.collection.get(quiz_id):
            self.collection[quiz_id] = {}
        answers_mass = []

        if formset.is_valid:
            for form in formset.forms:
                print(form.cleaned_data['id'].id)
                if form.cleaned_data['checked']:
                    answers_mass.append(form.cleaned_data['id'].id)
            self.collection[quiz_id][question_id] = answers_mass
            self.save()

    def clear(self, quiz_id):
        if self.collection.get(str(quiz_id)):
            del self.collection[str(quiz_id)]
            self.save()

    def results(self, quiz_id):
        # try:
        #     return len(self.collection[str(quiz_id)])
        # except:
        #     return 0
        quiz = deepcopy(self.collection[str(quiz_id)])
        right_answers = {}
        print(quiz)
        total = 0
        for key, question in quiz.items():
            right_answers[key] = self.get_right_answers(key)
            if question == self.get_right_answers(key):
                total += 1
        return {'amount': total, 'user_answers': quiz, 'right_answers': right_answers}

    def save(self):
        self.request.session.modified = True


    def get_right_answers(self, question_id):
        question = Question.objects.get(id=question_id)
        right_answers = []
        for var in question.variants.all():
            if var.checked:
                right_answers.append(var.id)
        return right_answers

        