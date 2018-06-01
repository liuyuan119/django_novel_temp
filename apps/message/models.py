from django.db import models


class UserMessage(models.Model):
    name = models.CharField(max_length=32, verbose_name="用户名")
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.CharField(max_length=500, verbose_name="留言信息")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "用户留言信息"
        verbose_name_plural = verbose_name
        db_table = "user_message"
        ordering = ["-create_time"]
