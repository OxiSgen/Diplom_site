from django.db import models


# Create your models here.


class News(models.Model):
    news_text = models.CharField(max_length=200)
    news_url = models.CharField(max_length=200)
    news_hype_rate = models.PositiveSmallIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_text