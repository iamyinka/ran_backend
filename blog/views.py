# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm

def post_list(request):
    posts_list = Post.published.all()
    recent_posts = Post.published.all()[0:4]
    paginator = Paginator(posts_list, 2)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/post/list.html", {"posts": posts, "recent_posts": recent_posts})

def post_detail(request, year, month, day, post):
    recent_posts = Post.published.all()[0:4]
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post Found")
    
    return render(request, "blog/post/detail.html", {"post": post, "recent_posts": recent_posts})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'iamyinka@dev.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, "blog/post/share.html", {
        "post": post,
        "form": form,
        "sent": sent
    })