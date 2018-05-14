from django.db import models
import PIL


# Create your models here.
class Article(models.Model):
    a_title = models.CharField('标题', max_length=20)
    a_content = models.TextField('内容')
    a_create_time = models.DateTimeField('发表时间', auto_now_add=True)
    a_update_time = models.DateTimeField('修改时间', auto_now=True, null=True)
    abstract = models.CharField('摘要', max_length=200, blank=True, null=True, )

    class Meta:
        db_table = 'article'


