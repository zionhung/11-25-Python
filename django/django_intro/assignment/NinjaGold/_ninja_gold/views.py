from django.shortcuts import render, redirect
import random
import datetime

def randomNum(start, end):
    num = random.randrange(start, end)
    return num

def earnOrAdd():
    chance = randomNum(0,2)
    if chance == 1:
        return True
    else:
        return False

def addActivity(request, num, action, location):
    timestamp = datetime.datetime.now()
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, timestamp)
            request.session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'Enterd acasino and lost %d gold... Ouch %s' % (num, timestamp)
            request.session['activity'].append(['lost', lost])
        else:
            print('error')
    elif location == 'farm':
        request.session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        request.session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        request.session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    else:
        print('error')
    request.session.save()

# Create your views here.
def index(request):
    if request.session.get('total_gold') == None:
        request.session['total_gold'] = 0
    if request.session.get('activity') == None:
        request.session['activity'] = []
    return render(request, 'index.html')

def process_money(request):
    hiddenInput = request.POST['hidden']
    if hiddenInput == 'farm':
        farmNum = randomNum(10,20)
        request.session['total_gold'] += farmNum
        addActivity(request, farmNum, 'earned', 'farm')
    elif hiddenInput == 'cave':
        caveNum = randomNum(5,10)
        request.session['total_gold'] += caveNum
        addActivity(request, caveNum, 'earned', 'cave')
    elif hiddenInput == 'house':
        houseNum = randomNum(2,5)
        request.session['total_gold'] += houseNum
        addActivity(request, houseNum, 'earned', 'house')
    elif hiddenInput == 'casino':
        casinoNum = randomNum(0,50)
        chance = earnOrAdd()
        if chance:
            request.session['total_gold'] += casinoNum
            addActivity(request, casinoNum, 'earned', 'casino')
        else:
            request.session['total_gold'] -= casinoNum
            addActivity(request, casinoNum, 'lost', 'casino')
    return redirect('/')
