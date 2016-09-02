from django.db import models

# Create your models here.
# 目标站点
class Dest(models.Model):
    webname = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    # order_user = models.ForeignKey()


# 抓取的新闻表
class News(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    post_date = models.DateTimeField()
    content = models.TextField()
