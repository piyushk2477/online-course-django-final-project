# Capturing the two required screenshots

These screenshots must be taken from your own running Django app after creating sample data; this repository does not include fabricated screenshots.

## `03-admin-site.png`
1. Run `python manage.py migrate` and `python manage.py createsuperuser`.
2. Start `python manage.py runserver` and sign in at `http://127.0.0.1:8000/admin/`.
3. Capture the admin index showing both **Authentication and Authorization** and **Onlinecourse** sections.
4. Save the screenshot as `screenshots/03-admin-site.png` and commit it to this repository.

## `07-final.png`
1. In admin, create a Course, at least one Lesson, Questions for that lesson, and answer Choices for every question. Mark exactly one choice per question as correct.
2. Open the course from the homepage, open the lesson mock exam, select the correct answers, and submit.
3. Capture the result page showing **Congratulations**, the score, and the exam results.
4. Save it as `screenshots/07-final.png` and commit it to this repository.

Use real screenshots of the app in a browser. Do not use a mockup or a screenshot of code as a substitute.
