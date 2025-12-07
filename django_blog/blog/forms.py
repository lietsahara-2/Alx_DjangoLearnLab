from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def clean_tags(self):
        tag_string = self.cleaned_data.get("tags", "")
        names = [t.strip() for t in tag_string.split(",") if t.strip()]
        tags = []

        for name in names:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)

        return tags


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
