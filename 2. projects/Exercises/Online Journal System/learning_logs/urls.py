"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all topics.
    url(r'^topic/$', views.topics, name='topics'),

    # Detail page for a sngle topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Page for adding a new topic
    url(r'^new_topics/$', views.new_topic, name='new_topic'),

]