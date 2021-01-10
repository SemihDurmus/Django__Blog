from django import forms
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Select")

    class Meta:
        model = Post
        fields = (
            'title', 'image', 'content', 'category', 'status'
        )


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Write your comment here', 'height': '300px'}))

    class Meta:
        model = Comment
        fields = ('content', )
