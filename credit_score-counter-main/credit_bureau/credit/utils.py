# credit/utils.py

from .models import UserResponse, Question

def calculate_credit_score(user):
    responses = UserResponse.objects.filter(user=user)
    total_score = 0

    for response in responses:
        question = response.question
        answer = response.response
        if answer == 'A':
            total_score += question.score_a
        elif answer == 'B':
            total_score += question.score_b
        elif answer == 'C':
            total_score += question.score_c
        elif answer == 'D':
            total_score += question.score_d

    return total_score
