from django.shortcuts import render, HttpResponse, redirect
from .models import Blogs, Contact, BlogComment,Carosel
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homePage(request):

    allblogs = Blogs.objects.all().order_by('-Date')
    carImages = Carosel.objects.all()

    dic = {"blogs": allblogs,"car":carImages}

    return render(request, "index.html", dic)


def BlogPage(request, id):
    pos = Blogs.objects.filter(id=id).first()
    comments = BlogComment.objects.filter(post=pos)
    pst = {"blogs": pos, "comments": comments}
    return render(request, "blogPage.html", pst)


def search(request):

    query = request.GET['search']

    search = Blogs.objects.filter(title__icontains=query)
    s = {"search": search, "q": query}

    return render(request, "search.html", s)


def loginUser(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        luser = authenticate(username=username, password=password)
        if luser is not None:
            login(request, luser)
            messages.success(request, "logged In")
            return redirect('/')
        else:
            messages.error(request, "Please check your username or password")
            return redirect('login')

    return render(request, "login.html")


def signup(request):

    if request.method == "POST":

        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=fname, last_name=lname)
        user.save()
        messages.success(request, 'Account successful created')

    return render(request, "signup.html")


def logoutUser(request):

    logout(request)
    messages.success(request, 'successfully logged out')
    return redirect("login")
    return HttpResponse("logged out")


def category(request, category):

    cat = Blogs.objects.filter(category=category).order_by('-Date')

    catDic = {"cat": cat}

    return render(request, "category.html", catDic)


def contactUs(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        contact = Contact(name=name, email=email,
                          number=number, message=message)
        contact.save()
        messages.success(request, 'Thanks for contacting us')
        redirect("contact")

    return render(request, "contact.html")


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postid = request.POST.get('postSno')
        post = Blogs.objects.get(id=postid)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/Blogs/{post.id}")
