from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

time = strftime("%H:%M %p", gmtime())

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request,'index.html')

def process(request):
    # ALWAYS print the form first to see what's in it
    print(request.POST['which_form'])

    if request.POST['which_form'] == 'pirate_booty':
        rand = random.randint(-50,50)
        request.session['gold'] += int(rand)
        if rand >= 0:
            request.session['location'] = (f"Earned {rand} golds from the Treasure Chest! {time}")
            request.session['activities'].append(request.session['location'])
        if rand < 0:
            request.session['location'] = (f"Lose {rand} Pirate says: Don't touch my booty! {time}")
            request.session['activities'].append(request.session['location'])
        return redirect('/')

    if request.POST['which_form'] == 'cave':
        rand = random.randint(1,50)
        request.session['gold'] += int(rand)
        request.session['location'] = (f"Mined {rand} golden nuggets from the cave! {time}")
        request.session['activities'].append(request.session['location'])
        return redirect('/')

    if request.POST['which_form'] == 'bank_safe':
        rand = random.randint(1,50)
        request.session['gold'] += int(rand)
        request.session['location'] = (f"Robbed {rand} gold from the vault! {time}")
        request.session['activities'].append(request.session['location'])
        return redirect('/')

    if request.POST['which_form'] == 'casino':
        rand = random.randint(-50,50)
        request.session['gold'] += int(rand)
        if rand >= 0:
            request.session['location'] = (f"Won {rand} gold from Blackjack! {time}")
            request.session['activities'].append(request.session['location'])
        if rand < 0:
            request.session['location'] = (f"Lost {rand} Stop Gambling! {time}")
            request.session['activities'].append(request.session['location'])
        return redirect('/')

# def room_42(request):
#     if 'gold' not in request.session:
#         request.session['gold'] = 0
#     if request.POST['which_form'] == 'room_42':
#         request.session['location'] = "Welcome to Room 42"
#     return redirect('/')


# def gold(request)
#     request.session['gold'] = 

def clear(request):
    request.session.clear()
    return redirect('/')
