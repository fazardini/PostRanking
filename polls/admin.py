from django.contrib import admin

from polls.models import Post, Poll

admin.site.register(Post)
admin.site.register(Poll)