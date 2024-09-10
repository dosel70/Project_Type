from django.db import models

class Member(models.Model):
    member_email = models.CharField(max_length=50, null=False, blank=False)
    member_password = models.CharField(max_length=128, null=False, blank=False)  # 해시된 비밀번호는 길이가 큽니다

    class Meta:
        db_table = 'tbl_member'
