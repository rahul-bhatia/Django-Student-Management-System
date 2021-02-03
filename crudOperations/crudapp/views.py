from django.shortcuts import render,redirect
from .models import studentModel
from .form import studentForm
# Create your views here.
def home(request):
	data=studentModel.objects.all()
	return render(request,'home.html',{'data':data})

def create(request):
	if request.method=='POST':
		f=studentForm(request.POST)
		if f.is_valid():
			f.save()
			fm=studentForm()
			return render(request,'create.html',{'fm':fm,'msg':'record added'})
		else:
			return render(request,'create.html',{'fm':f,'msg':'check errors'})
	else:
		fm=studentForm()
		return render(request,'create.html',{'fm':fm})

def delete(request,id):
	ds=studentModel.objects.get(rno=id)
	ds.delete()
	return redirect('home')

def edit(request,id):
	es=studentModel.objects.get(rno=id)
	print(es.name)
	fm=studentForm(initial={'rno':es.rno,'name':es.name,'marks':es.marks})
	fm.fields['rno'].widget.attrs['readonly']= True
	return render(request,'update.html',{'fm':fm})

def update(request):
	if request.method=='POST':
		r=request.POST.get('rno')
		n=request.POST.get('name')
		m=request.POST.get('marks')
		s=studentModel.objects.get(rno=r)
		s.name=n
		s.marks=m
		s.save()
		fm=studentForm()
		return render(request,'create.html',{'fm':fm,'msg':'Record updated'})
	else:
		fm=studentForm()
		return render(request,'create.html',{'fm':fm})