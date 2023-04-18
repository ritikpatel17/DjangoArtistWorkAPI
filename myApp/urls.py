from django.urls import path
from .views import ArtistList, ArtistDetail, WorkList, WorkDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/artists/', ArtistList.as_view()),
    path('api/artists/<int:pk>/', ArtistDetail.as_view()),
    path('api/works/', WorkList.as_view()),
    path('api/works/<int:pk>/', WorkDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

