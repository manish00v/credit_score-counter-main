# views.py

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, UserResponse
from .utils import calculate_credit_score

@login_required
def question_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        print("Form submitted")  # Debugging statement
        for question in questions:
            response = request.POST.get(f'question_{question.id}')
            if response:
                UserResponse.objects.create(
                    user=request.user,
                    question=question,
                    response=response
                )
        print("Redirecting to results")  # Debugging statement
        return redirect('result_view')
    return render(request, 'credit/questions.html', {'questions': questions})


@login_required
def result_view(request):
    score = calculate_credit_score(request.user)
    return render(request, 'credit/results.html', {'score': score})


# credit