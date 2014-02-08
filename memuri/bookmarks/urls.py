from django.conf.urls import patterns, include, url


urlpatterns = patterns('bookmarks.views',
    url(r'^user/(?P<username>[-\w]+)/$', 'bookmark_user',
        name='bookmarks_bookmark_user'),
    url(r'^create/$', 'bookmark_create', name='bookmarks_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'bookmark_edit', name='bookmarks_bookmark_edit'),
    url(r'^$', 'bookmark_list', name='bookmarks_bookmark_list'),
)