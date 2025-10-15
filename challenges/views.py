from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SubmissionForm
from .models import Challenge

@login_required
def challenges_view(request):
    challenges = Challenge.objects.all().order_by('start_date')
    return render(request, 'challenges.html', {'challenges': challenges})

@login_required
def submit_challenge(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.save()
            return redirect('challenges')
    else:
        form = SubmissionForm()
    return render(request, 'c_submission.html', {'form': form})



