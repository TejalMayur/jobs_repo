from django.shortcuts import render
from testapp.forms import Studentform
# Create your views here.
def studentview(request):
    submitted=False
    if request.method == 'POST':
        form=Studentform(request.POST)
        if form.is_valid():
            print('Form validation successs and priting data')
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
            print('Age:',form.cleaned_data['age'])
            sname=form.cleaned_data['name']
            submitted=True
    form=Studentform()
    return render(request,'testapp/input.html',{'form':form,'submitted':submitted})
