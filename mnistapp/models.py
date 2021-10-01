from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=13) #학습된 모델이 사진을 보고 판단하여 넣어줄 이름
    image = models.ImageField(default='media/default_image.png') #image 는 url 형식으로 저장
