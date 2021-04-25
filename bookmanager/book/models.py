from django.db import models

# Create your models here.
"""
1.我们的模型需要集成models.Model类，不然我们需自己写方法
2.系统会自动给我们添加一个主键
3.字段
    字段名=model.类型（选项)
    字段名就是数据表的字段名
    字段名不要使用python和mysql的关键字
"""
class BookInfo(models.Model):
    # 系统会自动给我们添加一个主键
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
# 先把人物复制过来，后期讲原理
class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)