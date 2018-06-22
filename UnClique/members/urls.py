from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView


from members.views import home, late_registration

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
        name='member_signup')
]