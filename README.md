# DiaAI 💕🔍

DiaAI is a web-based diabetes prediction platform built with Django and powered by the TabNet machine learning model. Users can enter health-related data to receive an instant prediction of whether they are at risk of diabetes.

---

## 🚀 Features

- 🎯 Accurate diabetes prediction using TabNet
- 🧼 Auto-calculation of BMI and DPF (Diabetes Pedigree Function)
- 📋 Multi-step form for user-friendly input
- 💻 Responsive design with animations
- 📊 Results displayed with clear messaging
- 📩 Contact form + thank you page

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **ML Model**: TabNet (pickle format)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default for Django)
- **Styling**: Custom CSS with animations

---

## 📆 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sj4107/DiaAI.git
   cd DiaAI
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

6. **Visit the app**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🤖 Model Info

- TabNet model trained on Pima Indians Diabetes dataset
- Saved as `tabnet_model.pkl`
- Used for binary classification: `Diabetic` or `Not Diabetic`

---

## 🖼️ Screenshots (Optional)

> _Include images of your homepage, form steps, and result page here_

---

## 🙇‍♂️ Author

- **Name**: [Your Name]
- **GitHub**: [@Sj4107](https://github.com/Sj4107)

---

## 📄 License

MIT License – feel free to fork, improve, and share!

