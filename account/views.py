from django.http import HttpResponse    
from django.shortcuts import render    
from django.contrib.auth import authenticate, login    
from .forms import LoginForm 
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from lostitem.models import lostitem,finditem


@login_required
def dashboard(request):
     if request.method == "POST":
        claimpla = request.POST.get('claimpla')
        info = request.POST.get('info')
        twz = lostitem.objects.create(category='校园卡',claimpla=claimpla,info=info)
        twz.save()
     lostitems = lostitem.objects.filter(category="校园卡")
     return render(request,'account/xiaoyuanka.html',{'lostitems':lostitems})
    

def user_login(request):        
    if request.method == 'POST':            
        form = LoginForm(request.POST)            
        if form.is_valid():                
            cd = form.cleaned_data                
            user = authenticate(username=cd['username'],
                                password=cd['password'])                
            if user is not None:                    
                if user.is_active:                        
                    login(request, user)                        
                    return HttpResponse('Authenticated successfully')
                else:                        
                    return HttpResponse('Disabled account')
            else:            
                return HttpResponse('Invalid login')        
    else:            
        form = LoginForm()        
    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                         'account/register_done.html',
                         {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                 'account/register.html',
                 {'user_form': user_form})
def shouji(request):
     if request.method == "POST":
        claimpla = request.POST.get('claimpla')
        info = request.POST.get('info')
        shouji = lostitem.objects.create(category='手机',claimpla=claimpla,info=info)
        shouji.save()
     lostitems = lostitem.objects.filter(category="手机")
     return render(request,'account/shouji.html',{'lostitems':lostitems})
 
def shuben(request):
     if request.method == "POST":
        claimpla = request.POST.get('claimpla')
        info = request.POST.get('info')
        shuben = lostitem.objects.create(category='书本',claimpla=claimpla,info=info)
        shuben.save()
     lostitems = lostitem.objects.filter(category="书本")
     return render(request,'account/shuben.html',{'lostitems':lostitems})
 
def upan(request):
     if request.method == "POST":
        claimpla = request.POST.get('claimpla')
        info = request.POST.get('info')
        shuben = lostitem.objects.create(category='U盘',claimpla=claimpla,info=info)
        shuben.save()
     lostitems = lostitem.objects.filter(category="U盘")
     return render(request,'account/upan.html',{'lostitems':lostitems})
 
def zhengjian(request):
     if request.method == "POST":
        claimpla = request.POST.get('claimpla')
        info = request.POST.get('info')
        zhengjian = lostitem.objects.create(category='证件',claimpla=claimpla,info=info)
        zhengjian.save()
     lostitems = lostitem.objects.filter(category="证件")
     return render(request,'account/zhengjian.html',{'lostitems':lostitems})
def yusan(request):
     if request.method == "POST":
        claimpla = request.POST.get('claimpla')
        info = request.POST.get('info')
        zhengjian = lostitem.objects.create(category='雨伞',claimpla=claimpla,info=info)
        zhengjian.save()
     lostitems = lostitem.objects.filter(category="雨伞")
     return render(request,'account/yusan.html',{'lostitems':lostitems})
def qita(request):
     if request.method == "POST":
        claimpla = request.POST.get('claimpla')
        info = request.POST.get('info')
        zhengjian = lostitem.objects.create(category='其他',claimpla=claimpla,info=info)
        zhengjian.save()
     lostitems = lostitem.objects.filter(category="其他")
     return render(request,'account/qita.html',{'lostitems':lostitems})
 
def sxiaoyuanka(request):
     if request.method == "POST":
         lostpla = request.POST.get('lostpla')
         info = request.POST.get('info')
         tele = request.POST.get('tele')
         xiaoyuanka = finditem.objects.create(category='校园卡',lostpla=lostpla,info=info,tele=tele)
         xiaoyuanka.save()
     finditems = finditem.objects.filter(category="校园卡")
     return render(request,'finditem/xiaoyuanka.html',{'finditems':finditems})
 
def sshouji(request):
     if request.method == "POST":
         lostpla = request.POST.get('lostpla')
         info = request.POST.get('info')
         tele = request.POST.get('tele')
         xiaoyuanka = finditem.objects.create(category='手机',lostpla=lostpla,info=info,tele=tele)
         xiaoyuanka.save()
     finditems = finditem.objects.filter(category="手机")
     return render(request,'finditem/shouji.html',{'finditems':finditems})
def sshuben(request):
     if request.method == "POST":
         lostpla = request.POST.get('lostpla')
         info = request.POST.get('info')
         tele = request.POST.get('tele')
         xiaoyuanka = finditem.objects.create(category='书本',lostpla=lostpla,info=info,tele=tele)
         xiaoyuanka.save()
     finditems = finditem.objects.filter(category="书本")
     return render(request,'finditem/shuben.html',{'finditems':finditems})
def supan(request):
     if request.method == "POST":
         lostpla = request.POST.get('lostpla')
         info = request.POST.get('info')
         tele = request.POST.get('tele')
         xiaoyuanka = finditem.objects.create(category='U盘',lostpla=lostpla,info=info,tele=tele)
         xiaoyuanka.save()
     finditems = finditem.objects.filter(category="U盘")
     return render(request,'finditem/upan.html',{'finditems':finditems})

def szhengjian(request):
     if request.method == "POST":
         lostpla = request.POST.get('lostpla')
         info = request.POST.get('info')
         tele = request.POST.get('tele')
         xiaoyuanka = finditem.objects.create(category='证件',lostpla=lostpla,info=info,tele=tele)
         xiaoyuanka.save()
     finditems = finditem.objects.filter(category="证件")
     return render(request,'finditem/zhengjian.html',{'finditems':finditems})
 
def syusan(request):
     if request.method == "POST":
         lostpla = request.POST.get('lostpla')
         info = request.POST.get('info')
         tele = request.POST.get('tele')
         xiaoyuanka = finditem.objects.create(category='雨伞',lostpla=lostpla,info=info,tele=tele)
         xiaoyuanka.save()
     finditems = finditem.objects.filter(category="雨伞")
     return render(request,'finditem/yusan.html',{'finditems':finditems})
  
def sqita(request):
     if request.method == "POST":
         lostpla = request.POST.get('lostpla')
         info = request.POST.get('info')
         tele = request.POST.get('tele')
         xiaoyuanka = finditem.objects.create(category='其他',lostpla=lostpla,info=info,tele=tele)
         xiaoyuanka.save()
     finditems = finditem.objects.filter(category="其他")
     return render(request,'finditem/qita.html',{'finditems':finditems})
def xiaoli(request):
     return render(request,'information/xiaoli.html')
def zuoxibiao(request):
     return render(request,'information/zuoxibiao.html')
def lifein(request):
     return render(request,'information/lifein.html')
 
def taolunqu(request):
     return render(request,'index.html')