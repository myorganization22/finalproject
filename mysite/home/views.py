from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator


# auth
def create(request):
    if request.method == 'GET':
        # if request.user.username == 'Date44' or request.user.username == 'admin123':
        return render(request, 'home/create.html', context={
            'form': PostForm()
        })
        # else:
        #     return render(request, 'account/403.html', context={})
    elif request.method == 'POST':
        field_form = PostForm(request.POST, request.FILES)
        field_form.save()
        return redirect('/')


# auth
def delete(request, post_id):
    data = dict()
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        data['post'] = post
        return render(request, 'home/delete.html', context=data)
    elif request.method == 'POST':
        post.delete()
        return redirect('/')


def details(request, post_id):
    data = dict()
    data['post'] = Post.objects.get(id=post_id)
    return render(request, 'home/details.html', context=data)


# edit
def edit(request, post_id):
    data = dict()
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        # if request.user.username == 'Date44' or request.user.username == 'admin123':
        data['form'] = PostForm(instance=post)
        data['post'] = post
        return render(request, 'home/edit.html', context=data)
        # else:
        #     return render(request, 'account/403.html', context={})
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.about = form.cleaned_data['about']
            post.content = form.cleaned_data['content']
            post.author = form.cleaned_data['author']
            post.source = form.cleaned_data['source']
            post.image = form.cleaned_data['image']
            post.save()
        return redirect('/')



def index(request):
    data = dict()  # Словарь данных
    all_posts = Post.objects.all()
    data['posts'] = all_posts

    paginator = Paginator(all_posts, 5)
    page_numder = request.GET.get('page')
    page_obj = paginator.get_page(page_numder)
    data['page_obj'] = page_obj

    return render(request, 'home/index.html', context=data)