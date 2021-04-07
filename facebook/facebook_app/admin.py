from django.contrib import admin
from facebook_app.models import FriendRequest, FriendList
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Coment)
#admin.site.register(FriendList)
#admin.site.register(FriendRequest)

class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    readonly_fields = ['user']

    class Meta:
        model = FriendList

admin.site.register(FriendList, FriendListAdmin)

class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender__username','sender__email', 'receiver__email', 'receiver__username']

    class Meta:
        model = FriendRequest

admin.site.register(FriendRequest, FriendRequestAdmin)