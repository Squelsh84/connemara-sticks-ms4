from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


def blogs(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    # Display 3 products per page.
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Blog', 'page_obj': page_obj}
    return render(request, 'blogs.html', context, {"post_list": post_list})


def blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog.html', {'post': post,
                                         'comments': comments,
                                         'new_comment': new_comment,
                                         'comment_form': comment_form})
