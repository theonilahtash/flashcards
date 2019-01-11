from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^new/profile$',views.add_profile,name='add_profile'),
    url(r'^new/card$', views.new_card, name='new-card'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



