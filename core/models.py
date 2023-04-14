from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 추상화하여 마이그레이션 실행시 테이블 생성 X
        abstract = True