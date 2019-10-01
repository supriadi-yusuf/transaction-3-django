from django.conf.urls import url
from .views import save_with_exception, save_without_exception, \
    non_atomic, outside, exception_in_try_except_block, \
    outer_inner_1, outer_inner_2, atomic_1, atomic_2, atomic_3, \
    atomic_4, atomic_5, atomic_6, atomic_7, atomic_8, atomic_9
#from django.contrib import admin

urlpatterns = [
    url(r'^exception/$', save_with_exception),
    url(r'^no_exception/$', save_without_exception),
    url(r'^non_atomic/$', non_atomic),
    url(r'^outside/$', outside),
    url(r'^exception_in_try_except_block/$', exception_in_try_except_block),
    url(r'^outer_inner_1/$', outer_inner_1),
    url(r'^outer_inner_2/$', outer_inner_2),
    url(r'^atomic_1/$', atomic_1),
    url(r'^atomic_2/$', atomic_2),
    url(r'^atomic_3/$', atomic_3),
    url(r'^atomic_4/$', atomic_4),
    url(r'^atomic_5/$', atomic_5),
    url(r'^atomic_6/$', atomic_6),
    url(r'^atomic_7/$', atomic_7),
    url(r'^atomic_8/$', atomic_8),
    url(r'^atomic_9/$', atomic_9),
]
