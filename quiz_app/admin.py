from django.contrib import admin

from quiz_app.models import Quiz, Question, Variant

# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


class VarInline(admin.StackedInline):
    model = Variant
    

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [VarInline, ]

# @admin.register(Variant)
# class VariantAdmin(admin.ModelAdmin):
#     pass