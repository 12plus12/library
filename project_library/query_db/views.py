from django.shortcuts import render
from django.http import HttpResponse
from query_db import models


# Create your views here.
def index(request):
    if request.method == "POST":
        author_name = request.POST.get("authorname", None)
        book_name = request.POST.get("bookname", None)

        if author_name and book_name:
            try:
                models.AuthorInfo.objects.get(name=author_name)
            except Exception as e:
                models.AuthorInfo.objects.create(
                    name=author_name
                )

            author_id = models.AuthorInfo.objects.get(name=author_name).id

            models.BookInfo.objects.create(
                name=book_name,
                author_id=author_id
            )

    book_list = list()
    book_obj = models.BookInfo.objects.all()
    for book in book_obj:
        book_list.append({'bookid':book.id, 'bookname':book.name, 'authorname':book.author.name})

    return render(request, "demo.html", {"book_list":book_list})


def remove(request, book_id):
    """根据指定book_id删除"""
    # if request.method == "DELETE":
    try:
        book = models.BookInfo.objects.get(id=book_id)
    except Exception as e:
        pass
    else:
        book.delete()

    return index(request)
