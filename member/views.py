from django.contrib.auth.hashers import make_password
from pyexpat.errors import messages
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from member.serializers import MemberSerializer


# Create your views here.
class MemberCheckIdView(APIView):
    def get(self, request):
        member_id = request.GET['member-id']
        is_duplicated = Member.objects.filter(member_id=member_id).exists()
        return Response({'isDup': is_duplicated})

class MemberView(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_email' : data['member_email'],
            'member_password' : data['member_password']
        }

        member = Member.objects.filter(member_email=data['member_email'], member_password=data['member_password'])
        url = 'ai:manufact'
        if member.exists():
            request.session['member'] = MemberSerializer(member.first()).data
            return redirect('ai:manufact')

        return redirect(url)

class RegisterView(View):
    def get(self, request):
        context = {
            'memberEmail': request.GET.get('member_email'),
            'id': request.GET.get('id')
        }
        return render(request, 'login/register.html', context)

    @transaction.atomic
    def post(self, request):
        data = request.POST
        member_email = data['member_email']
        password1 = data['member_password1']
        password2 = data['member_password2']

        # 서버 측 비밀번호 확인
        if password1 != password2:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'login/register.html', {'member_email': member_email})

        # 비밀번호 해싱
        hashed_password = make_password(password1)

        # Member 객체 생성 및 저장
        Member.objects.create(member_email=member_email, member_password=hashed_password)
        messages.success(request, '회원가입이 성공적으로 완료되었습니다.')
        return redirect('member:login')