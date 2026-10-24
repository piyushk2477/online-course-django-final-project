# Online Course Django Final Project

A Django application for browsing online courses, viewing lessons, taking mock exams, and reviewing exam results.

## Setup

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the course list and `/admin/` for the Django administration site.

## Exam flow

Open a course, choose a lesson, take the mock exam, and submit answers. The result page displays the score and correct answers.

## Screenshots for the assignment

Run the app locally, add course/lesson/question/choice data in `/admin/`, and capture the actual admin page as `screenshots/03-admin-site.png` and a successful result page as `screenshots/07-final.png`. Screenshots should be captured from the running application, not fabricated.
