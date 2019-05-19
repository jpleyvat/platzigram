"""Post forms."""

#Django
from django import forms

#Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Form settings."""

    class Meta:
        """Form settings"""

        model = Post
        fields = Postfields = ('user', 'profile', 'title', 'photo')