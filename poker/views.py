from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .holdem import Poker
from .forms import CreateTableForm
from .models import Player, Table
import sys, random

debug = False
number_of_players = 4
poker = Poker(number_of_players, debug)
poker.shuffle()
poker.cut(random.randint(1,51))
players_hand = poker.distribute()
community_cards = []

# Create your views here.

def show_index(request):
    return render(request, "poker/index.html")
    
def show_pre_flop(request):
    return render(request, "poker/pre_flop.html", {"players_hand" : players_hand})
    
def show_flop(request):
    flop = poker.getFlop()
    community_cards.append(flop)
    return render(request, "poker/flop.html", {"players_hand" : players_hand, "community_cards" : community_cards})
    
def show_turn(request):
    turn = poker.getOne()
    community_cards.append(turn)
    return render(request, "poker/turn.html", {"players_hand" : players_hand, "community_cards" : community_cards})
    
def show_river(request):
    river = poker.getOne()
    community_cards.append(river)
    return render(request, "poker/river.html", {"players_hand" : players_hand, "community_cards" : community_cards})
    
@login_required
def create_table(request):
    if request.method=="POST":
        form = CreateTableForm(request.POST)
        table = form.save(commit=False)
        table.owner = request.user
        table.save()
        return redirect(get_table)
    else:
        form = CreateTableForm()
        return render(request, "poker/create_table.html", {'form': form})
        
def find_table(request):
    tables = Table.objects.filter(owner=request.user)
    return render(request, "poker/find_table.html", {"tables" : tables})

def get_table(request, name):
    table = Table.objects.get(name=name)
    return render(request, "poker/get_table.html", {"table" : table})
    


    