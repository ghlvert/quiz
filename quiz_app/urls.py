from django.urls import path, include

from quiz_app.views import index, quiz_detail ,question_processing

urlpatterns = [
    path('', index, name='home'),
    path('quiz/<int:quiz_id>', quiz_detail, name='quiz_detail'),
    path('question_processing/<int:quiz_id>/<int:question_id>', question_processing, name='question_processing'),
    path('api/', include('quiz_app.api.urls')),
]
