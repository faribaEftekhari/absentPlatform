from django.db import models

class student(models.Model):
    fullname=models.CharField(max_length=70)
    classId=models.ForeignKey('classNumber',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.fullname

class classNumber(models.Model):
    classname=models.CharField(max_length=70)

DAY_CHOICES=[(str(x),str(x)) for x in range(1, 32)]
MONTH_CHOICE=(
('مهر','مهر'),
('آبان','آبان'),
('آذر','آذر'),
('دی','دی'),
('بهمن','بهمن'),
('اسفند','اسفند'),
('فروردین','فروردین'),
('اردیبهشت','اردیبهشت'),
('خرداد','خرداد'),

)
YEAR_CHOICES=[(str(x),str(x)) for x in range(1400,1403)]
DELAY=(
('تاخیر','تاخیر'),
('غیبت','غیبت')
)
class absentStudent(models.Model):
    studentId=models.ForeignKey('student',on_delete=models.CASCADE,null=True)
    day=models.CharField(max_length=6, choices=DAY_CHOICES, default='1')
    month=models.CharField(max_length=15,choices=MONTH_CHOICE,default='mehr')
    year=models.CharField(max_length=6, choices=YEAR_CHOICES, default='1400')
    description=models.TextField(default=' ',blank=True)
    delay=models.CharField(max_length=10,choices=DELAY,default='ندارد')
