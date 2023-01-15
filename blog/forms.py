from django import forms
from .models import Comment


class CommentForm(forms.ModelForm, ):
    class Meta:
        model = Comment
        fields = ('name', 'body')

    def __init__(self, user="None", *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control', 'readonly': True, 'value': user}
        self.fields['body'].widget.attrs = {'placeholder': 'Comment here...', 'class': 'form-control', 'rows': '5'}
