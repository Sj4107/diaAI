from django.contrib import admin
from .models import Contact,DiabetesPrediction

admin.site.register(Contact)
@admin.register(DiabetesPrediction)
class DiabetesPredictionAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'glucose', 'bmi', 'dpf', 'pregnancies', 'result', 'created_at')
    search_fields = ('name', 'result')
    list_filter = ('gender', 'result', 'created_at')
