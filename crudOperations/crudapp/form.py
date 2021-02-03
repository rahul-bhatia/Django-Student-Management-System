
from django import forms
from .models import studentModel

class studentForm(forms.ModelForm):
	class Meta:
		model=studentModel
		fields=['rno','name','marks']