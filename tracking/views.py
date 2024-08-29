from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Import this
from .models import TimeEntry
from .forms import TimeEntryForm

@login_required  # Apply this decorator
def log_time(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            time_entry = form.save(commit=False)
            time_entry.user = request.user  # Associate with logged-in user
            time_entry.save()
            return redirect('time_entries')
    else:
        form = TimeEntryForm()
    return render(request, 'tracking/log_time.html', {'form': form})

@login_required  # Apply this decorator
def time_entries(request):
    entries = TimeEntry.objects.filter(user=request.user)  # Filter by user
    return render(request, 'tracking/time_entries.html', {'entries': entries})
