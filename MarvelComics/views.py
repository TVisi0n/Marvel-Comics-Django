from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComicForm
from .models import Comic
from bs4 import BeautifulSoup
import requests

def marvelcomics_home(request):
    return render(request, "MarvelComics/marvelcomics_home.html",)

def marvelcomics_create(request):
    form = ComicForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marvelcomics_home')
    content = {'form': form}
    return render(request, 'MarvelComics/marvelcomics_create.html', content)

def marvelcomics_shelf(request):
    comic = Comic.addComics.all()
    content = {'comic': comic}
    return render(request, "MarvelComics/marvelcomics_shelf.html", content)

def marvelcomics_details(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    content = {'comic': comic}
    return render(request, "MarvelComics/marvelcomics_details.html", content)

def marvelcomics_update(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    form = ComicForm(data=request.POST or None, instance=comic)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../shelf')
    content = {'form': form, 'comic': comic}
    return render(request, "MarvelComics/marvelcomics_update.html", content)

def marvelcomics_delete(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    if request.method == 'POST':
        comic.delete()
        return redirect("../../shelf")
    content = {'comic': comic}
    return render(request, "MarvelComics/marvelcomics_delete.html", content)

def marvelcomics_bs(request):
    page = requests.get("https://www.coverbrowser.com/covers/marvel-comics")
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.find_all('img')
    url = 'https://d29xot63vimef3.cloudfront.net'
    images = []
    for i in img:
        src = i.get('src')
        text = url + src
        images.append(text)
    content = {'images': images}
    return render(request, "MarvelComics/marvelcomics_bs.html", content)

def marvelcomics_api(request):
    return render(request, "MarvelComics/marvelcomics_api.html")
