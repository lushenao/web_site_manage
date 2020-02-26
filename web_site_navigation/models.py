from django.db import models

# Create your models here.

class web_class(models.Model):
    cid = models.AutoField(primary_key=True)
    class_name = models.CharField(verbose_name='网站所属类名称',max_length=20,unique=True)
    ctime = models.DateTimeField(verbose_name='创建日期',auto_now_add=True,null=True)
    uptime = models.DateTimeField(verbose_name='修改日期',auto_now=True,null=True)
    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = '网站所属类'  # 改变表在admin中的名字
        verbose_name_plural = '网站所属类'

class web_class_obj(models.Model):
    oid = models.AutoField(primary_key=True)
    obj_name = models.CharField(verbose_name='网站所属组名称',max_length=40,unique=True)
    obj_environment_choice = {
        (1,'生产环境'),
        (2,'测试环境'),
    }

    obj_environment = models.IntegerField(verbose_name='网站所属组环境',choices=obj_environment_choice,default=1)
    
    ctime = models.DateTimeField(verbose_name='创建日期',auto_now_add=True,null=True)
    uptime = models.DateTimeField(verbose_name='修改日期',auto_now=True,null=True)
    
    web_class = models.ForeignKey('web_class',to_field='cid',on_delete=models.CASCADE,verbose_name='网站所属类',)
    def __str__(self):
        return self.obj_name
    class Meta:
        verbose_name = '网站所属组'  # 改变表在admin中的名字
        verbose_name_plural = '网站所属组'

class web_site(models.Model):
    site_name = models.CharField(verbose_name='网站名称',max_length=26,unique=True)
    site_url = models.CharField(verbose_name='网站URL',max_length=255,unique=True)
    ctime = models.DateTimeField(verbose_name='创建日期',auto_now_add=True,null=True)
    uptime = models.DateTimeField(verbose_name='修改日期',auto_now=True,null=True)

    web_class_obj = models.ForeignKey('web_class_obj',to_field='oid',on_delete=models.CASCADE,verbose_name='网站所属组',)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = '网站URL'  # 改变表在admin中的名字
        verbose_name_plural = '网站URL'



