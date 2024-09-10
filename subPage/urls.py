from django.urls import path

from subPage import views
from subPage.views import subPageView

app_name = 'subPage'

urlpatterns = [
    path('main/', subPageView.as_view(), name='main')
]