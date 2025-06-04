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

    def clear(self, quiz_id):
        if self.collection.get(str(quiz_id)):
            del self.collection[str(quiz_id)]
            self.save()

    def count(self, quiz_id):
        try:
            return len(self.collection[str(quiz_id)])
        except:
            return 0

    def save(self):
        self.request.session.modified = True

    