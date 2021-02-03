from django.db import models

# Create your models here.
class studentModel(models.Model):
	rno=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=10)
	marks=models.IntegerField()
	
	def ___str___(self):
		return self.name