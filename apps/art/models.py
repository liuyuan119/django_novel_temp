from django.db import models
from django.utils import timezone


# create_date = models.DateTimeField(auto_now_add=True)
# update_date = models.DateTimeField(auto_now=True)

# Eg:
# class Class(models.Model):
#     name = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.name
#
#
# class Student(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#     phone = models.CharField(max_length=15)
#     cls_id = models.ForeignKey(Class)
#
#     def __str__(self):
#         return self.name


# 文章标签类
class Tag(models.Model):
    t_name = models.CharField(max_length=255, verbose_name="标签名")
    t_info = models.CharField(max_length=300, verbose_name="标签描述")
    t_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建时间")

    class Meta:
        db_table = "tag"
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.t_name


# 文章类
class Art(models.Model):
    a_title = models.CharField(max_length=255, verbose_name="文章标题")
    a_info = models.CharField(max_length=300, verbose_name="备注")
    a_content = models.TextField(verbose_name="文章内容")
    a_img = models.ImageField(null=True, blank=True, upload_to="uploads", verbose_name="文章图片")
    a_addtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建时间")
    a_updatetime = models.DateTimeField(default=timezone.now, verbose_name="更新时间")
    a_tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.a_title

    class Meta:
        db_table = "art"
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-a_addtime']
