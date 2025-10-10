from django.shortcuts import render,redirect
from books.models import Book as BookModel
from categories.models import Category as CategoryModel
from reviews.models import Review as ReviewModel

def homeView(r):
    books=BookModel.objects.all().order_by('total_borrowed_time')
    categorys=CategoryModel.objects.all()
    reviews=ReviewModel.objects.all()
    for re in reviews:
        print(re.user.user_acc.user_image)
    return render(r,"index.html",{"books":books,"categorys":categorys,"reviews":reviews})
def redirect_home(request, exception):
    return redirect('home')