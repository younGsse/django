from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from ..models import Comment, Reply
from ..forms import ReplyForm

@login_required(login_url='common:login')
def reply_create(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.create_time = timezone.now()
            reply.author = request.user
            reply.comment = comment
            reply.save()
            return redirect('{}#reply_{}'.format(resolve_url('community:detail', fiction_id=reply.comment.fiction.id), reply.id))
    else:
        form = ReplyForm()
    context = {'form': form}
    return render(request, 'community/reply_form.html', context)

@login_required(login_url='common:login')
def reply_modify(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.user != reply.author:
        messages.error(request, "Not authority")
        return redirect('community:detail', fiction_id=reply.comment.fiction.id)
    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.modified_time = timezone.now()
            reply.author = request.user
            reply.save()
            return redirect('{}#reply_{}'.format(resolve_url('community:detail', fiction_id=reply.comment.fiction.id), reply.id))
    else:
        form = ReplyForm(instance=reply)
    context = {'form': form}
    return render(request, 'community/reply_form.html', context)

@login_required(login_url='common:login')
def reply_delete(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.user != reply.author:
        messages.error(request, "Not authority")
        return redirect('community:detail', fiction_id=reply.comment.fiction.id)
    else:
        reply.delete()
    return redirect('community:detail', fiction_id=reply.comment.fiction.id)
