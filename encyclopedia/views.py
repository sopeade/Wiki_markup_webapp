from django.shortcuts import render, reverse
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
import re
import random
from markdown2 import markdown_path, markdown, Markdown


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/pages.html", {"page": markdown(util.get_entry(title)), "heading": title})
    else:
        return HttpResponseNotFound("The requested page was not found.")


def search(request):
    search = request.POST["q"]
    search_cap = request.POST["q"].capitalize()
    search_up = request.POST["q"].upper()

    for page in util.list_entries():

        if search in page:
            return HttpResponseRedirect(reverse("title", args=(search,)))

        elif search_cap in page:
            return render(request, "encyclopedia/matches.html",
                          {"matches": page})

        elif search_up in page:
            return render(request, "encyclopedia/matches.html",
                          {"matches": page})
        else:
            pass

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def new(request):
    return render(request, "encyclopedia/new_page.html")


def check_new(request):
    pg_title = request.POST["title"]
    content = request.POST["content"]

    if pg_title in util.list_entries():
        return HttpResponse("The Title entered already exists")
    else:
        util.save_entry(pg_title, content)
        return HttpResponseRedirect(reverse("title", args=(pg_title,)))


def editing(request, heading):
    return render(request, "encyclopedia/edit_page.html", {"edited": util.get_entry(heading), "heading": heading})


def random_page(request):
    x = util.list_entries()
    selected = random.choice(x)
    return render(request, "encyclopedia/pages.html", {"page": markdown(util.get_entry(selected)), "heading": selected})
