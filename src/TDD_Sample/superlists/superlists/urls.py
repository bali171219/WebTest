from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/(\d+)/$', 'lists.views.list_view', name='list_view'),
    url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    url(r'^lists/(\d+)/add$', 'lists.views.add_item', name='add_item'),
)
