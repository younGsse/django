from django.urls import path

from .views import base_views, fiction_views, comment_views, reply_views

app_name = 'community'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:fiction_id>/', base_views.detail, name='detail'),

    path('fiction/create/', fiction_views.fiction_create, name='fiction_create'),
    path('fiction/modify/<int:fiction_id>/', fiction_views.fiction_modify, name='fiction_modify'),
    path('fiction/delete/<int:fiction_id>/', fiction_views.fiction_delete, name='fiction_delete'),

    path('comment/create/<int:fiction_id>/', comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),

    path('reply/create/comment/<int:comment_id>/', reply_views.reply_create, name='reply_create'),
    path('reply/modify/comment/<int:reply_id>/', reply_views.reply_modify, name='reply_modify'),
    path('reply/delete/comment/<int:reply_id>/', reply_views.reply_delete, name='reply_delete'),
]
