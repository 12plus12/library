from django.shortcuts import render
from django.http import HttpResponse
from query_db import models


# Create your views here.
def index(request):
    if request.method == "POST":
        models.BookInfo.objects.create(
            name=request.POST.get("bookname", None)
        )

    book_list = models.BookInfo.objects.all()
    return render(request, "demo.html", {"book_list":book_list})
