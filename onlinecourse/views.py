from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Lesson, Question, Submission


def course_list(request):
    return render(request, 'onlinecourse/course_list.html', {'courses': Course.objects.all()})


def course_details(request, course_id):
    course = get_object_or_404(Course.objects.prefetch_related('lessons'), pk=course_id)
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})


def mock_exam(request, lesson_id):
    lesson = get_object_or_404(Lesson.objects.select_related('course').prefetch_related('questions__choices'), pk=lesson_id)
    return render(request, 'onlinecourse/mock_exam.html', {'lesson': lesson})


def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson.objects.prefetch_related('questions__choices'), pk=lesson_id)
    if request.method != 'POST':
        return redirect('onlinecourse:mock_exam', lesson_id=lesson.id)

    questions = list(lesson.questions.all())
    answers = {}
    score = 0
    for question in questions:
        selected_id = request.POST.get(f'question_{question.id}')
        answers[str(question.id)] = selected_id or ''
        if selected_id and question.choices.filter(pk=selected_id, is_correct=True).exists():
            score += 1

    submission = Submission.objects.create(
        user=request.user if request.user.is_authenticated else None,
        lesson=lesson, score=score, total_questions=len(questions), answers=answers,
    )
    return redirect('onlinecourse:show_exam_result', submission_id=submission.id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission.objects.select_related('lesson__course'), pk=submission_id)
    questions = submission.lesson.questions.prefetch_related('choices').all()
    results = []
    for question in questions:
        selected_id = submission.answers.get(str(question.id))
        selected_choice = question.choices.filter(pk=selected_id).first() if selected_id else None
        correct_choice = question.choices.filter(is_correct=True).first()
        results.append({'question': question, 'selected_choice': selected_choice, 'correct_choice': correct_choice,
                        'is_correct': bool(selected_choice and selected_choice.is_correct)})
    return render(request, 'onlinecourse/exam_result.html', {'submission': submission, 'results': results})
