from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from products.models import News, Products, Comment

#
#
@login_required(login_url='login')
def new_comment(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        Comment.objects.create(
            author=request.user,
            products=product,
            body=request.POST['body'],
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('product:detail', product_id)
    return HttpResponse("add comment")
#
#
@login_required(login_url='login')
def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.info(request, 'Successfully Deleted!')
        return redirect('product:detail', product_id)
    return redirect('product:detail', product_id)


@login_required(login_url='login')
def ProductsView(request):
    products = Products.objects.all()
    q = request.GET.get('q', '')
    if q:
        products = products.filter(title__icontains=q)
    return render(request, "index.html", {'products': products})


@login_required(login_url='login')
def NewsView(request):
    news = News.objects.all()
    q = request.GET.get('q', '')
    if q:
        news = news.filter(title__icontains=q)
    return render(request, "news.html", {'news': news})


@login_required(login_url='login')
def Product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
