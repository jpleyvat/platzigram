
"""User admin clases"""

# jjuan
# platzigram

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
"""from django.contrib.admin.options import StackedInline"""

#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""

    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture'
    )
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        ('Profile', {

            'fields': (
                ('user', 'picture'),
                
            )
        }),
        ('Extra Info', {
            'fields':(
                ('phone_number', 'website'),
                ('biography',)
            )
        }),
        ('Metadata',{
            'fields':(('created', 'modified'),),
        })

    )

    readonly_fields = ('created', 'modified', 'user')


class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add Profile admin to base user admin"""

    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts Admin"""

    list_display = (
        'user',
        'profile',
        'title',
        'photo',
        'created',
        'modified',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)