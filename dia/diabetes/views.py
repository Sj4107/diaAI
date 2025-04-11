from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

from .models import Contact, DiabetesPrediction

import os
import numpy as np
import torch
import joblib
from pytorch_tabnet.tab_model import TabNetClassifier


# -------------------- Home --------------------
def home(request):
    return render(request, 'diabetes/index.html')


# -------------------- Contact --------------------
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        suggestion = request.POST.get('suggestion', '')
        feedback = request.POST.get('feedback', '')

        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            suggestion=suggestion,
            feedback=feedback
        )

        subject = "Thanks for reaching out!"
        message = f"Hi {name},\n\nThanks for your message and feedback!\nWe'll get back to you soon.\n\n- Team"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

        return render(request, 'diabetes/thankyou.html', {'name': contact.name})

    return render(request, 'diabetes/contact.html')


# -------------------- Result --------------------
def result_view(request, name, result):
    return render(request, 'diabetes/result.html', {
        'name': name,
        'result': result
    })


# -------------------- Predict --------------------
# -------------------- Predict --------------------
def predict_view(request):
    if request.method == 'POST':
        try:
            model_path = os.path.join(settings.BASE_DIR, 'diabetes', 'ml_models', 'tabnet_model.pkl')

            # Patch torch.load temporarily for joblib
            original_torch_load = torch.load

            def cpu_loader(*args, **kwargs):
                kwargs['map_location'] = torch.device('cpu')
                return original_torch_load(*args, **kwargs)

            torch.load = cpu_loader
            model = joblib.load(model_path)
            torch.load = original_torch_load  # Restore original torch.load
            model.device = torch.device('cpu')  # Ensure model runs on CPU

        except Exception as e:
            return render(request, 'diabetes/predict.html', {
                'error': f"⚠️ Model loading error: {str(e)}"
            })

        # --- Extract form fields ---
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        glucose = request.POST.get('glucose')
        bmi = request.POST.get('bmi')
        dpf = request.POST.get('dpf')
        pregnancies = request.POST.get('pregnancies', '0')

        # --- Validation ---
        if not all([name, gender, age, glucose, bmi, dpf]):
            return render(request, 'diabetes/predict.html', {
                'error': 'Please fill in all required fields.'
            })

        try:
            age = float(age)
            glucose = float(glucose)
            bmi = float(bmi)
            dpf = float(dpf)
            pregnancies = float(pregnancies) if gender == "female" else 0.0  # Set to 0 if male
        except ValueError:
            return render(request, 'diabetes/predict.html', {
                'error': 'Please enter valid numerical values.'
            })

        # --- Predict ---
        features = np.array([[pregnancies, glucose, bmi, dpf, age]], dtype=np.float32)

        try:
            with torch.no_grad():
                prediction = model.predict(features)[0]
        except Exception as e:
            return render(request, 'diabetes/predict.html', {
                'error': f"⚠️ Prediction failed: {str(e)}"
            })

        result = "Yes" if prediction == 1 else "No"

        # --- Save to DB ---
        DiabetesPrediction.objects.create(
            name=name,
            gender=gender,
            age=age,
            glucose=glucose,
            bmi=bmi,
            dpf=dpf,
            pregnancies=pregnancies,
            result=result
        )

        return HttpResponseRedirect(reverse('result', args=[name, result]))

    return render(request, 'diabetes/predict.html')
