from django import template

register = template.Library()


@register.simple_tag()
def get_colour_of_answer(variant_id, question_id:int, user_answers, right_answers):
    if variant_id in right_answers[str(question_id)] and variant_id in user_answers[str(question_id)]:
        return 'green'
    elif variant_id in right_answers[str(question_id)] and variant_id not in user_answers[str(question_id)]:
        return 'purple'
    elif variant_id not in right_answers[str(question_id)] and variant_id in user_answers[str(question_id)]:
        return 'red'
    else:
        return 'black'
    