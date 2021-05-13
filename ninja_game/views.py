from django.shortcuts import render, redirect
import random
from time import gmtime, localtime, strftime

game_type = {
    "farm":{
        "range":(10,20),
    },
    "cave":{
        "range":(5,10),
    },
    "house":{
        "range":(2,5),
    },
    "casino":{
        "range":(-50,50),
    },
}

def index(request):

    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime()),
    }
    if not "gold" in request.session or not "activities" in request.session:
        
        request.session["gold"] = 0
        request.session["activities"] = []

    return render(request, 'index.html', context)

def process_money(request):
    game = request.POST["game"]
    earn_range = game_type[game]["range"]
    earning = random.randint(earn_range[0],earn_range[1])
    result = ""
    amount = 0

    if earning > 0:
        amount = earning
        result = f"You earned {amount} at the {game}"
    elif earning == 0:
        amount = earning
        result = f"You didn't win or lose anything at the {game}"
    else:
        amount = earning
        neg = amount * -1
        result = f"You lost {neg} at the {game}"

    request.session["gold"] += amount
    request.session["activities"].insert(0,result)
        

    return redirect('/')

def reset_activity(request):
    request.session["activities"] = []

    return redirect('/')

def reset_gold(request):
    request.session["gold"] = 0

    return redirect('/')

def reset_all(request):
    request.session["gold"] = 0
    request.session["activities"] = []

    return redirect('/')