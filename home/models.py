from django.db import models
from datetime import datetime, timedelta

def now_plus_15min():
    return datetime.now() + timedelta(minutes = 15)

class Grafana(models.Model):
    CHART_CHOICES = (
        ('', '[ -- 데이터를 선택하세요 -- ]'),
        ('Kmong', (
            ('http://13.124.181.8:23000/d/7LYL66iWk/kmong-dashboard?orgId=1&from=1558165782765&to=1558166646765&theme=light&panelId=2&fullscreen', '페이지별 전환율 및 이탈율'),
            ('http://13.124.181.8:23000/d/7LYL66iWk/kmong-dashboard?orgId=1&from=1558165782765&to=1558166646765&theme=light&panelId=6&fullscreen', '사용자별 페이지 분석'),
            ('http://13.124.181.8:23000/d/7LYL66iWk/kmong-dashboard?orgId=1&from=1558165782765&to=1558166646765&theme=light&panelId=4&fullscreen', '사용기기별 페이지 뷰'),
            ('http://13.124.181.8:23000/d/7LYL66iWk/kmong-dashboard?orgId=1&from=1558165782765&to=1558166646765&theme=light&panelId=8&fullscreen', '운영체제 버전별 페이지 뷰'),
            ('http://13.124.181.8:23000/d/7LYL66iWk/kmong-dashboard?orgId=1&from=1558165782765&to=1558166646765&theme=light', '전체 대시보드'),
        )),
        ('NC_Soft', (
            ('http://13.124.181.8:23000/d/LmYTJnWZk/nc-dashboard?orgId=1&from=1558160725797&to=1558161589797&theme=light&panelId=2&fullscreen', '사용자별 채집 횟수 모니터링'),
            ('http://13.124.181.8:23000/d/LmYTJnWZk/nc-dashboard?orgId=1&from=1558160725797&to=1558161589797&theme=light&panelId=5&fullscreen', '사용자별 PK 횟수 모니터링'),
            ('http://13.124.181.8:23000/d/LmYTJnWZk/nc-dashboard?orgId=1&from=1558160725797&to=1558161589797&theme=light&panelId=6&fullscreen', '사용자별 경험치 획득량 모니터링'),
            ('http://13.124.181.8:23000/d/LmYTJnWZk/nc-dashboard?orgId=1&from=1558160725797&to=1558161589797&theme=light&panelId=4&fullscreen', '사용자별 아이템 획득량 모니터링'),
            ('http://13.124.181.8:23000/d/LmYTJnWZk/nc-dashboard?orgId=1&from=1558160725797&to=1558161589797&theme=light', '전체 대시보드'),
        )),
        ('Zigzag', (
            ('http://13.124.181.8:23000/d/-VU-kZWZk/zigzag-dashboard?orgId=1&from=1558163561840&to=1558164333269&theme=light&panelId=6&fullscreen', '사용자별 최근 활동 내역'),
            ('http://13.124.181.8:23000/d/-VU-kZWZk/zigzag-dashboard?orgId=1&from=1558163561840&to=1558164333269&theme=light&panelId=8&fullscreen', '사용자별 접속당 평균 활동 수'),
            ('http://13.124.181.8:23000/d/-VU-kZWZk/zigzag-dashboard?orgId=1&from=1558163561840&to=1558164333269&theme=light&panelId=10&fullscreen', '상품 카테고리별 매출 조회'),
            ('http://13.124.181.8:23000/d/-VU-kZWZk/zigzag-dashboard?orgId=1&from=1558163561840&to=1558164333269&theme=light&panelId=4&fullscreen', '검색 키워드별 조회 수'),
            ('http://13.124.181.8:23000/d/-VU-kZWZk/zigzag-dashboard?orgId=1&from=1558163561840&to=1558164333269&theme=light', '전체 대시보드'),
        )),
    )
    embed_url = models.URLField()
    chart = models.CharField(max_length=500, choices=CHART_CHOICES)
    start_time = models.DateTimeField(default=datetime.now) 
    end_time = models.DateTimeField(default=now_plus_15min) 