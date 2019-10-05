from django.urls import path
from .views import (CreateSellRequest,RequestUpdateView,CollectableList, CollectableDetails, UserCreateAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns=[
path('login/', TokenObtainPairView.as_view() , name='login'),
path('register/', UserCreateAPIView.as_view(), name='register'),
path('collectable/list/', CollectableList.as_view(), name='collectable-list'),
path('collectable/detail/<int:collectable_id>/', CollectableList.as_view(), name='collectable-detail'),
path('sellrequest/', CreateSellRequest.as_view(), name='sell-request'),
path('sellrequest/update/<int:sellrequest_id>', RequestUpdateView.as_view(), name='update-sellrequest'),

]

