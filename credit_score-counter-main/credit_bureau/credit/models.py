# credit/models.py

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    score_a = models.IntegerField()  # Points for option A
    score_b = models.IntegerField()  # Points for option B
    score_c = models.IntegerField()  # Points for option C
    score_d = models.IntegerField()  # Points for option D

    def __str__(self):
        return self.question_text

class UserResponse(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=1)  # Stores 'A', 'B', 'C', or 'D'

    def __str__(self):
        return f"{self.user} - {self.question} - {self.response}"
