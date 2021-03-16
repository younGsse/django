from django import forms
from community.models import Fiction, Comment, Reply

class FictionForm(forms.ModelForm):
    class Meta:
        model = Fiction
        fields = ['fiction_subject', 'fiction_text']
        labels = {
            'fiction_subject': 'subject',
            'fiction_text': 'content',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        labels = {
            'comment_text': 'content',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']
        labels = {
            'reply_text': 'content'
        }
