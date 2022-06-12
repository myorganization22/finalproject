from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index),
    path("index", index),
    path("create", create),
    re_path(r"^delete/(?P<post_id>[0-9]+)$", delete),
    re_path(r"^edit/(?P<post_id>[0-9]+)$", edit),
    re_path(r"^details/(?P<post_id>[0-9]+)$", details),
]
