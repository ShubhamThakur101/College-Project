from django.shortcuts import redirect,render
from django.views import View
from .models import Table_details
from .forms import AddDetailsForm
# Create your views here.

class Home(View):
    def get(self,request):
        td_data = Table_details.objects.all()
        return render(request, 'core/home.html',{'tDdata':td_data})
    
class Add_Details(View):
    def get(self,request):
        fm = AddDetailsForm()
        return render(request, 'core/add_details.html',{'form':fm})
    
    def post(self,request):
            fm = AddDetailsForm(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('/')
            else:
                return render(request, 'core/add_details.html',{'form':fm})
            
class Delete_Tdata(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        tDdata = Table_details.objects.get(id=id)
        tDdata.delete()
        return redirect('/')