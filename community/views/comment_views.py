from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from ..models import Fiction, Comment
from ..forms import CommentForm

@login_required(login_url='common:login')
def comment_create(request, fiction_id):
    fiction = get_object_or_404(Fiction, pk=fiction_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_time = timezone.now()
            comment.fiction = fiction
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('community:detail', fiction_id=fiction.id), comment.id))
    else:
        form = CommentForm()
    context = {'fiction': fiction, 'form': form}
    return render(request, 'community/fiction_detail.html', context)

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "Not authority")
        return redirect('community:detail', fiction_id=comment.fiction.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modified_time = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('community:detail', fiction_id=comment.fiction.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'community/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "Not authority")
    else:
        comment.delete()
    return redirect('community:detail', fiction_id=comment.fiction.id)
