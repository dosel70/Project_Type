from django.urls import path

from member.views import MemberView, RegisterView, MemberCheckIdView
from subPage import views
from subPage.views import subPageView

app_name = 'member'

urlpatterns = [
    path('login/', MemberView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('check-id/', MemberCheckIdView.as_view(), name='check-id')
]