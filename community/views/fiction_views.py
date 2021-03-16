from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Fiction
from ..forms import FictionForm


@login_required(login_url='common:login')
def fiction_create(request):
    if request.method == 'POST':
        form = FictionForm(request.POST)
        if form.is_valid():
            fiction = form.save(commit=False)
            fiction.author = request.user
            fiction.create_time = timezone.now()
            fiction.save()
            return redirect('community:index')
    else:
        form = FictionForm()
    context = {'form': form}
    return render(request, 'community/fiction_form.html', context)

@login_required(login_url='common:login')
def fiction_modify(request, fiction_id):
    fiction = get_object_or_404(Fiction, pk=fiction_id)
    if request.user != fiction.author:
        messages.error(request, "Do not have authority.")
        return redirect('community:detail', fiction_id=fiction_id)
    if request.method == "POST":
        form = FictionForm(request.POST, instance=fiction)
        if form.is_valid():
            fiction = form.save(commit=False)
            fiction.author = request.user
            fiction.modified_time = timezone.now()
            fiction.save()
            return redirect('community:detail', fiction_id=fiction.id)
    else:
        form = FictionForm(instance=fiction)
    context = {'form': form}
    return render(request, 'community/fiction_form.html', context)

@login_required(login_url='common:login')
def fiction_delete(request, fiction_id):
    fiction = get_object_or_404(Fiction, pk=fiction_id)
    if request.user != fiction.author:
        messages.error(request, "Not authority")
        return redirect('community:detail', fiction_id=fiction.id)
    fiction.delete()
    return redirect('community:index')
