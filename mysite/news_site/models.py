from django.db import models


# Create your models here.


class News(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    news_text = models.CharField(max_length=200, blank=True, null=True)
    news_url = models.CharField(max_length=200, blank=True, null=True)
    news_hype_rate = models.PositiveSmallIntegerField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.news_text