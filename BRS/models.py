from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField('用户名', max_length=20, default='')
    password = models.CharField('密码', max_length=18, default='')
    userPhone = models.CharField('电话', max_length=18, default='')
    userEmail = models.CharField('邮箱', max_length=18, default='')
    userMajor = models.CharField('专业', max_length=18, default='')
    userGrade = models.CharField('年级', max_length=18, default='')
    userGender = models.CharField('性别', max_length=18, default='')
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '%s_%s' % (self.username, self.password)

