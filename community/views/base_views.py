from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from ..models import Fiction

from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    fiction_list = Fiction.objects.order_by('-create_time')
    if kw:
        fiction_list = fiction_list.filter(
            Q(fiction_subject__icontains=kw) |
            Q(fiction_text__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(comment__author__username__icontains=kw)
        ).distinct()

    paginator = Paginator(fiction_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'fiction_list': page_obj,
        'page': page,
        'kw': kw,
    }
    return render(request, 'community/fiction_list.html', context)

def detail(request, fiction_id):
    fiction = get_object_or_404(Fiction, pk=fiction_id)
    context = {
        'fiction': fiction
    }
    return render(request, 'community/fiction_detail.html', context)
