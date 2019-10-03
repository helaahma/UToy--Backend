from django.urls import path

from .views import (CollectableList, CollectableDetails)

urlpatterns=[
path('collectable/list/', CollectableList.as_view(), name='collectable-list'),
path('collectable/detail/<int:collectable_id>/', CollectableList.as_view(), name='collectable-detail'),
]