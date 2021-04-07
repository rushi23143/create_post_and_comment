from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.sessions.models import Session
from django.contrib import auth
from .models import *

# Create your views here.
def navigate(request):
    if request.method == "POST":
        button = request.POST['button']
        if button == 'admin':
            return redirect('admin_login')
        elif button == 'user':
            return redirect('login')
    return render(request, 'navigate.html')

def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = User.objects.filter(email=email,password=password).count()
        if count >0:
            #request.session['is_logged'] = True
            request.session['user_id'] = User.objects.values('id').filter(email=email,password=password)[0]['id']
            return redirect('base')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


def register_user(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj = User(username=username,email=email,password=password)
        obj.save()
        messages.success(request, 'You are registered successfully')
        return redirect('login')
    return render(request, 'register_user')



def logout(request):
    auth.logout(request)
    return redirect('login')

def base(request):
    fetch_data = Blog.objects.all()
    #if request.session.has_key('is_logged'):
    return render(request, "base.html",{'data':fetch_data})
    #return redirect('login')

def create_post(request):
    if request.POST:
        good_name = request.POST['goodname']
        description = request.POST['description']
        title = request.POST['title']
        image = request.POST['image']
        user_id = request.session['user_id']
        obj = Blog(good_name=good_name,
                   description=description,
                   title=title,
                   image=image)
        obj.user_id_id = user_id
        obj.save()
        messages.success(request,"your post add successfully..")
        return redirect("base")
    return render(request, "create_post.html")



def readmore(request,id):
    if request.POST:
        message = request.POST['message']
        user_id = request.POST['user_id']
        post_id = id
        query = Coment(message=message)
        query.post_id_id = post_id
        query.user_id_id = user_id
        query.save()
    #return HttpResponse(str(id))
    data = Blog.objects.get(id=id)
    comment = Coment.objects.all().filter(post_id=id)
    return render(request, 'readmore.html',{'data':data, 'comments':comment})
"""
class friend_list(ListView):
    model = FriendList
    template_name = 'friend_list.html'

    def get(self, request):
        userss = User.objects.all()
        users = User.objects.all()
        return render(request, 'friend_list.html',{'users':users,'userss':len(userss)})


class friend_request(ListView):
    model = FriendRequest
    template_name = 'friend_request.html'

    #def get(self, request):
    #   return render(request, 'friend_request.html')

"""
#def friend_list(request):
#    return render(request, 'friend_list.html')
"""
def friend_request(request,id):
    from_user=request.user
    to_user=User.objects.get(id=id)
    frequest=FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return render("friend_list")

def accept_request(request,id):
    frequest=FriendRequest.objects.get(id=id)
    user1=request.user
    user2=frequest.from_user
    user1.friends.add(user2)
    user2.friends.add(user1)
    return redirect('friend_list')

"""
####### admin panel
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin@1234':
            return redirect('admin_panel')
        else:
            messages.info(request, 'password not matching........')
            return redirect('admin_login')
    else:
        return render(request, 'admin/admin_login.html')

def admin_panel(request):
    users = User.objects.all()
    blogs = Blog.objects.all()
    comments = Coment.objects.all()
    friendlist = FriendList.objects.all()
    friendrequest = FriendRequest.objects.all()
    return render(request, 'admin/admin_panel.html',{'users':len(users), 'blogs':len(blogs), 
                                                    'comments':len(comments), 'friendlist':len(friendlist),
                                                     'friendrequest':len(friendrequest)})

def admin_blog(request):
    blogss = Blog.objects.all()
    return render(request, "admin/admin_blog.html",{'blogss':blogss})

def admin_coment(request):
    commentss = Coment.objects.all()
    return render(request, "admin/admin_coment.html",{'commentss':commentss})

def admin_flist(request):
    frndlist = FriendList.objects.all()
    return render(request, "admin/admin_flist.html",{'frndlist':frndlist})

def admin_frequest(request):
    frndrequest = FriendRequest.objects.all()
    return render(request, "admin/admin_frequest.html",{'frndrequest':frndrequest})

def users(request):
    users = User.objects.all()
    return render(request, 'admin/users.html', {'users': users})
    #return render(request, "admin/users.html")


