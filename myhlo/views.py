from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import Contact
from .models import Service

# Create your views here.
def index(request):
    data={
        'title':'this is our website',
        'clist':[1,2,3,4,5]
    }
    return  render(request,"index.html",data)
   

def about(request):
    return render(request,"about.html")
   
def contact(request):
    if request.method=='POST':
        nm = request.POST.get('name')
        eml = request.POST.get('email')
        pn = request.POST.get('pnum')
        msg = request.POST.get('msg')
        print(">>>>>>>",nm, eml, pn, msg)
        user = Contact(name=nm, email=eml, pnumber=pn, message=msg)
        user.save()
    return render(request,"contact.html")

def post(request):
    return render(request,"post.html")
def userfrms(request):
    final_output=0
    try:

        if request.method=="GET":
                # n1=request.GET.get("num1")
                # n2=request.GET.get("num2")
                  n1=int(request.GET['num1'])
                  n2=int(request.GET["num2"])
                  final_output=n1+n2
                  print(final_output)
                  
                  
    except:
         pass
        
    return render(request,"userfrm.html",{'output':final_output,})

def cals(request):
    c=0
    try:
        if request.method=='POST':
            num1 =int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            opr= (request.POST.get('opr'))
            print(num1)
            print(num2)
            if opr=="+":
                  c=num1+num2
                  print(c)
            elif opr=="-":
                  c=num1-num2
                  print(c)
            
    except:
         pass
        
    return render(request,"calculator.html",{'output':c})

def evenodd(request):
    c=""
    if (request.POST.get("num1"))=="":
             return render(request,"evenodd.html",{'error':True})
          
    
    
    
    if request.method=="POST":
         num1=int(request.POST.get("num1"))
         if num1%2==0:
              c="evennumber"
         else:
              c="odd"
    
    return render(request,"evenodd.html",{'output':c})


def service(request):
    #  services=Service.objects.all()
    services=Service.objects.all().order_by('-service_title')[:3]
    if request.method=="GET":
         st=request.GET.get('servicename')
         if st!=None:
              services=Service.objects.filter(service_title__icontains=st)
            #   services=Service.objects.filter(service_title__icontains=st)
    data={
          "ser":services
     }
     
    return render(request,"service.html",data)