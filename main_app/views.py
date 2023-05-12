from django.shortcuts import render, redirect

from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Collectible
from .forms import ReviewsForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')






def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })




def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    reviews_form = ReviewsForm()
    return render(request, 'games/detail.html', {'game': game, 'reviews_form': reviews_form})

def add_review(request, game_id):
    form = ReviewsForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.game_id = game_id
        new_review.save()
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'


class GameUpdate(UpdateView):
    model = Game
    fields = ['genre', 'description']

class GameDelete(DeleteView):
    model = Game
    success_url ='/games/'


class CollectibleList(ListView):
    model = Collectible


class CollectibleDetail(DetailView):
    model = Collectible

class CollectibleCreate(CreateView):
    model = Collectible
    fields = '__all__'

class CollectibleUpdate(UpdateView):
  model = Collectible
  fields = '__all__'

class CollectibleDelete(DeleteView):
  model = Collectible
  success_url = '/collectibles/'