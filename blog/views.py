from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages


def post_list(request):
    posts = Post.published.all()

    paginator = Paginator(posts, 10)  # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {'posts': posts, page: 'pages'})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, user=request.user.username)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url() + '#' + str(new_comment.id))
        else:
            comment_form = CommentForm()

    return render(request, 'post_detail.html',
                  {'post': post, 'comments': comments, 'comment_form': CommentForm(user=request.user.username)})


def reply_page(request):
    if request.method == "POST":

        form = CommentForm(data=request.POST, user=request.user.username)
        if form.is_valid():
            post_id = request.POST.get('post_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            post_url = request.POST.get('post_url')  # from hidden input

            reply = form.save(commit=False)

            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url + '#' + str(reply.id))
        else:
            for error in list(form.errors.values()):
                messages.success(request, error)
    return redirect("/")
