from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'lists.views.list_view', name='list_view'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    url(r'^(\d+)/add$', 'lists.views.add_item', name='add_item'),
)
