from django.shortcuts import render, redirect
from .models import Post, Contact, Comment
from django.core.paginator import Paginator


def home_view(request):
    posts = Post.objects.filter(is_published=True)

    d = {
        'posts': posts
    }

    return render(request, 'index.html', context=d)


def about_view(request):
    return render(request, 'about.html')


def post_view(request, post_id):
    return render(request, 'contact.html')


def blog_view(request):
    data = request.GET
    category = data.get('category')
    page = data.get('page', 1)

    if category:
        posts = Post.objects.filter(is_published=True, category_id=category)
    else:
        posts = Post.objects.filter(is_published=True)

    paginator = Paginator(posts, 1)

    d = {
        'posts': paginator.page(page)
    }

    return render(request, 'blog.html', context=d)


def blog_detail_view(request, a):

    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(post_id=a, name=data['name'], email=data['email'], message=data['message'])
        obj.save()
        return redirect(f'/blog/{a}')
    post = Post.objects.filter(id=a).first()
    comments = Comment.objects.filter(post_id=a)

    return render(request, 'blog-single.html', context={'post': post, 'comments': comments})


def contact_view(request):

    data = request.POST
    if request.method == 'POST':
        obj = Contact.objects.create(name=data.get('name'), email=data.get('email'),
                                     message=data.get('message'), subject=data.get('subject'))

        obj.save()
        return redirect('/contact')
    return render(request, 'contact.html')


