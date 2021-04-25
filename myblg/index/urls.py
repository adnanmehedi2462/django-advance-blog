from django.urls import path

from . import views
app_name="index"
urlpatterns = [

    path('',views.index, name='index'),
    path('author/<name>',views.getauthor,name="author"),
    path('artical/<int:id>',views.getartical,name="single_post"),
    path('topic/<name>',views.gettopic,name="topic"),
    path('login',views.getlogin,name="login"),
    path('logout',views.getlogout,name="logout"),
    path('create',views.getcreate,name="create"),
    path('myprofile',views.getmyprofile,name="myprofile"),
    path('update/<int:pid>',views.getupdate,name="update"),
    path('delete/<int:did>',views.getdelete,name="delete"),
    path('signup',views.getsignup,name="signup"),
    path('showcat',views.getcat,name="showcatagory"),
    path('createcat/topic',views.getcata,name="createcatagor"),

    #accont activate
    path('activate/<uid>/<token>',views.activate,name="activate"),

    # json and xml

    path('json',views.getjson,name="json"),
    path('xml',views.getxml,name="xml"),









]

