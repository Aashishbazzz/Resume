from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'resume_html.html')

def complete(request):
    format_1=request.GET.get('format_1','off')
    my_first_name=request.GET.get('my_first_name','default')
    my_last_name=request.GET.get('my_last_name','default')
    my_mobile=request.GET.get('my_mobile','default')
    my_email=request.GET.get('my_email','default')
    my_address=request.GET.get('my_address','default')
    my_objective=request.GET.get('my_objective','default')
    my_qualify=request.GET.get('my_qualify','default')
    my_exp=request.GET.get('my_exp','default')
    my_achievements=request.GET.get('my_achievements','default')
    my_hobby=request.GET.get('my_hobby','default')
    params={'f_name':my_first_name,'l_name':my_last_name,'mob_no':my_mobile,'email':my_email,'address':my_address,'objective':my_objective,
            'qualification':my_qualify,'exp':my_exp,'achieve':my_achievements,'hobby':my_hobby}
    if( format_1=="on"):
        return render(request,'resume_complete_1.html',params)
    else:
        return render(request,'resume_complete_2.html',params)
    