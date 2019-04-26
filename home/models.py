from django.db import models
from datetime import datetime, timedelta

# Create your models here.

def now_plus_15min():
    return datetime.now() + timedelta(minutes = 15)

class Grafana(models.Model):
    embed_url = models.URLField()
    start_time = models.DateTimeField(default=datetime.now) # 현재 시간
    end_time = models.DateTimeField(default=now_plus_15min) # 현재 시간 + 15 분