from django.shortcuts import render
from django.views import View


class subPageView(View) :
    def get(self, request):
        return render(request, 'sub/sub.html')
