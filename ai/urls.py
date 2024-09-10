from django.urls import path

from ai.views import AiMainView, ManufactView, AlzhimeraView, ManufactResultView
from member.views import MemberView, RegisterView, MemberCheckIdView
from subPage import views
from subPage.views import subPageView

app_name = 'ai'

urlpatterns = [
    path('manufact/', AiMainView.as_view(), name='manufact'),
    path('manufact-sub/', ManufactView.as_view(), name='manufact-sub'),
    path('manufact-result/', ManufactResultView.as_view(), name='manufact-result'),
    path('alz/', AlzhimeraView.as_view(), name='alz')
]