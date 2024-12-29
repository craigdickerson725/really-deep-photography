from django.db import models
from django.shortcuts import render
from django.urls import path


# Define the FAQ model
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
