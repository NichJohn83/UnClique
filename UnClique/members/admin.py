from django.contrib import admin

from django.contrib import messages
# Register your models here.
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.urls import reverse

from members.models import Member




def shuffle(modeladmin, request, queryset):
    list = []
    for item in queryset:
        list.append(model_to_dict(item))

    print(list)
    return HttpResponseRedirect(reverse('members:member_display', kwargs={'memberlist': list}))
    #, args=memberlist)
    # return redirect('member_display', memberlist)


# def user_shuffle(modeladmin, request, queryset):
#     list = []
#     for item in queryset:
#         list.append(model_to_dict(item))
#
#     print(type(list))
#     return HttpResponseRedirect(reverse('members:member_display', kwargs={'memberlist': list}))


shuffle.short_description = "UnClique!"
# user_shuffle.short_description = "UnClique!"

class MemberAdmin(admin.ModelAdmin):
    ordering = ['first_name']
    actions = [shuffle]

class UserAdmin(admin.ModelAdmin):
    ordering = ['first_name']
    actions = [shuffle]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Member, MemberAdmin)
