from django.urls import path
from .views import (OnGoingBidDetail,OnGoingBidsList,BidView, CreateSellRequest,RequestUpdateView,DeleteCollectable,CollectableList, CollectableDetails, UserCreateAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns=[
path('login/', TokenObtainPairView.as_view() , name='login'),
path('register/', UserCreateAPIView.as_view(), name='register'),
path('collectable/list/', CollectableList.as_view(), name='collectable-list'),
path('collectable/detail/<int:collectable_id>/', CollectableDetails.as_view(), name='collectable-detail'),
path('collectable/delete/<int:collectable_id>/', DeleteCollectable.as_view(), name='collectable-delete'),
path('sellrequest/', CreateSellRequest.as_view(), name='sell-request'),
path('sellrequest/update/<int:sellrequest_id>/', RequestUpdateView.as_view(), name='update-sellrequest'),
path('bid/list/', OnGoingBidsList.as_view(), name='bid-list'),
path('bid/detail/<int:bid_id>/', OnGoingBidDetail.as_view(), name='bid-detail'),
path('bid/<int:collectable_id>/', BidView.as_view(), name='bid-create'),
]

