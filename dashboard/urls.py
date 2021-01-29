from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # user operations
    url(r'^dashboard/login/$', views.log_in, name='login'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^dashboard/signup/$', views.signup, name='signup'),
    url(r'^dashboard/account/$', views.account, name='account'),
    url(r'^dashboard/admin/$', views.admin, name='admin'),
    url(r'^dashboard/developer/$', views.developer, name='developer'),
    url(r'^dashboard/project_manager/$', views.project_manager, name='project_manager'),
    # Projects
    url(r'^dashboard/live_project/$', views.live_project, name='live_project'),
    url(r'^dashboard/project_archive/$', views.project_archive, name='project_archive'),
    url(r'^dashboard/project_hold/$', views.project_hold, name='project_hold'),
    # utilities
    url(r'^dashboard/contact/$', views.contact, name='contact'),
    url(r'^dashboard/about/$', views.about, name='about'),
]

