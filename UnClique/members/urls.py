from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from members.views import home, late_registration, display_members, graduation, unsubscribe_member, subscribe_member

urlpatterns =[
    url(r'home$', home, name='member_home'),
    url(r'login',
        LoginView.as_view(template_name="members/login_form.html"),
        name='member_login'),
    url(r'logout',
        LogoutView.as_view(),
        name='member_logout'),
    url(r'signup',
        late_registration,
        name='member_signup'),
    path(r'displaymembers/<memberlist>',
        display_members,
        name='member_display'
        ),
    path(r'complete/<memberlist>',
            graduation,
            name='unclique_complete'),
    path(r'subscribe',
            subscribe_member,
            name='sub'),
    path(r'unsubscribe',
            unsubscribe_member,
            name='unsub'),

    ]



#/<memberlist>'