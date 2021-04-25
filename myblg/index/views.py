
from django.shortcuts import render,get_object_or_404,redirect,Http404,HttpResponse
from django.http import HttpResponse
from .models import artical,categary,author,comment
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django .contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import CreateForm,createfrom,createauthor,createcomment,createcategory
from django.db.models import Q

#last add for advance send mail

from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail 
from .token import activation_token
#xml
from django.core import serializers
# Create your views here.
def index(request):
    post=artical.objects.all().order_by('-id')
    search=request.GET.get('q')
    if search:

        post=post.filter(

            Q(title__icontains=search)
        )


    paginator = Paginator(post, 5) # Show 8 contacts per page

    page = request.GET.get('page')
    total_page = paginator.get_page(page)
    context={
        "post":total_page,
    }
    return render(request,'index.html',context)
def getauthor(request,name):
    author_info=get_object_or_404(User, username=name)
    auth=get_object_or_404(author, name=author_info.id) #id is option , if u dont put this ,u have not face any problem
    all_post=artical.objects.filter(artical_author=auth.id) #id is option , if u dont put this ,u have not face any problem
    context={

        "auth":auth,
        "all_post":all_post,
    }


    return render(request,'profile.html',context)
 
def getartical(request,id):
    singlepost=get_object_or_404(artical,id=id)
    all_comment=comment.objects.filter(post=id).order_by('-id')
    related=artical.objects.filter(categary=singlepost.categary).order_by('-id').exclude(id=id)[:3]
    

    form=createcomment(request.POST or None)
    
    
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post= singlepost
        instance.save()
      
        return redirect('mainblogapp:index')
        
        
       
        
     

    context={

        "singlepost":singlepost,
        "related":related,
        "form":form,
        "all_comment":all_comment

    }
    return render(request,'singlepost.html',context)

def gettopic (request,name):
    cat=get_object_or_404(categary, name=name)
    same_post=artical.objects.filter(categary=cat.id).order_by('-id')

    
    paginator = Paginator(same_post, 2) # Show 8 contacts per page

    page = request.GET.get('page')
    total_page = paginator.get_page(page)
    context={
        "same_post":total_page,
        "cat":cat,


    }

    return render(request,"category.html",context)
def getlogin(request):
    if request.user.is_authenticated:
        return redirect('mainblogapp:index')
    else:


        if request.method=="POST":


            user=request.POST.get('user')
            password=request.POST.get('password')
        


            auth=authenticate(request,username=user,password=password)
            if auth is not None:

                login(request,auth)
                return redirect('mainblogapp:index')
            else:
                messages.error(request, 'Your email or password invalid!')



    return render(request,"login.html")


def getlogout(request):
    logout(request)
    messages.success(request, 'You are loged out!!!')
    return redirect('mainblogapp:index')


def getcreate(request):
    if request.user.is_authenticated:
        u=get_object_or_404(author,name=request.user.id)


        form=CreateForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.artical_author=u
            instance.save()
            
            messages.success(request, 'Your Post upload successfully!!')
            return redirect('mainblogapp:create')
        context={
            "form":form
        }
    else:
        return redirect('mainblogapp:index')


    return render(request,"create.html",context)



def getupdate(request,pid):
    if request.user.is_authenticated:
        u=get_object_or_404(author,name=request.user.id)
        post=get_object_or_404(artical,id=pid)


        form=CreateForm(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.artical_author=u
            instance.save()
            
            messages.success(request, 'Your Post updated successfully!!')
            return redirect('mainblogapp:myprofile')
        context={
            "form":form
        }
    else:
        return redirect('mainblogapp:index')


    return render(request,"create.html",context)




def getdelete(request,did):
    if request.user.is_authenticated:
        post=get_object_or_404(artical, id=did)
        post.delete()
        messages.success(request, 'Your Post deleted successfully!!')
        return redirect('mainblogapp:myprofile')


def getsignup(request):

    form=createfrom(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.is_active=False
        
        instance.save()
        site=get_current_site(request)
        mail_subject="Confermation message for Django Blog"

        message=render_to_string('confirm_email.html',{

            "user":instance,
            "domain":site.domain,
            "uid":instance.id,
            "token":activation_token.make_token(instance)
        })
        to_email=form.cleaned_data.get('email')
        to_list=[to_email]
        from_email=settings.EMAIL_HOST_USER
        send_mail(mail_subject,message,from_email,to_list,fail_silently=True)

        return HttpResponse("<h1>A confarmation massage was send to your email </h1>")
    

    
    
    return render(request,'signup.html',{"form":form})







def getmyprofile(request):


    if request.user.is_authenticated:
        user=get_object_or_404(User, id=request.user.id)
        author_profile=author.objects.filter(name=user.id)
        if author_profile:
            
            author_user=get_object_or_404(author, name=request.user.id)
            post=artical.objects.filter(artical_author=author_user.id).order_by('-id')
            post_slid=artical.objects.filter(artical_author=author_user.id).order_by('-id')[:3]

            return render(request,"myprofile.html",{"post":post,"user":author_user,"post_slid":post_slid,})
        else:

            form=createauthor(request.POST or None, request.FILES or None)

            if form.is_valid():
                
                instance=form.save(commit=False)
                instance.name=user
                instance.save()
                return redirect('mainblogapp:myprofile')
            return render(request,'createauthor.html',{"form":form})

    else:
        return redirect('mainblogapp:login')

def getcat(request):
    queary=categary.objects.all()
    return render(request,'showcat.html',{"queary":queary})

def getcata(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:

            form=createcategory(request.POST or None)

            if form.is_valid():

                instance=form.save(commit=False)
                instance.save()
                messages.success(request, 'category create successfully ')
                return redirect('mainblogapp:showcatagory')
        else:
            raise Http404("you are not auhtrize person to access this page")
    

    else:
        return redirect('mainblogapp:login')
 

    return render(request,"createcat.html",{"form":form})



def activate(request,uid,token):
    try:
        user=get_object_or_404(User,pk=uid)
    except:
        raise Http404("user not found")
    if user is not None and activation_token.check_token(user, token):
        user.is_active=True
        user.save()
        return HttpResponse("<h1>Your account is activated. Please <a href='/login'>Login</a></h1>")
    else:
        return HttpResponse("<h2>Invalid actavation Link </h2>")

def getjson(request):
    data=artical.objects.all()
    jsondata=serializers.serialize("json",data,indent=10)
    return HttpResponse(jsondata,content_type="application/json")




def getxml(request):

    data=artical.objects.all()
    xmldata=serializers.serialize("xml",data)
    return HttpResponse(xmldata,content_type="application/xml")
