from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    suggestion = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class DiabetesPrediction(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    glucose = models.FloatField()
    bmi = models.FloatField()
    dpf = models.FloatField()
    pregnancies = models.PositiveIntegerField(default=0)
    result = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
