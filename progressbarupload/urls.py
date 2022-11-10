# -*- coding: utf-8 -*-
from django.urls import path
from progressbarupload.views import upload_progress

urlpatterns = [
    path("upload_progress", upload_progress, name="upload_progress"),
]
