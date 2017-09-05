from django.db import models
from django.utils import timezone

class Post(models.Model):
	MONTH = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12'),)
	HOLIDAY = (('1', '日'),('2', '土日'),('3', '土日祝'),('4', 'その他'),)

	pr_bases = models.CharField(max_length=10)
	pr_month = models.CharField(max_length=1, choices=MONTH)
	pr_holiday_of_month = models.CharField(max_length=1, choices=HOLIDAY)
	pr_holiday_of_year = models.SlugField(max_length=3)
	pr_created_date = models.DateTimeField(default=timezone.now)
	pr_published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title