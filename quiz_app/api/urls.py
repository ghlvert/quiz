from django.urls import path
from rest_framework import routers

from quiz_app.api.views import QuizViewSet



router = routers.SimpleRouter()
router.register(r'quiz', QuizViewSet)

urlpatterns = router.urls