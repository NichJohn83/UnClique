from django.contrib import admin

from django.contrib import messages
# Register your models here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.urls import reverse

from members.models import Member




def shuffle(modeladmin, request, queryset):
    list = []
    for item in queryset:
        list.append(model_to_dict(item))

    # messages.add_message(request, messages.INFO, memberlist)

    return HttpResponseRedirect(reverse('members:member_display', args=[list]))
    #, args=memberlist)
    # return redirect('member_display', memberlist)



shuffle.short_description = "UnClique!"

class MemberAdmin(admin.ModelAdmin):
    ordering = ['first_name']
    actions = [shuffle]

admin.site.register(Member, MemberAdmin)