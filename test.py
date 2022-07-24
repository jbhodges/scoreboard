import time
import threading
import json

def fileWatcher():
    scores = ""
    scoresText = ""
    while True:
        f = open('scores.json')
        content = f.read()
        f.close()
        if content != scoresText:
            print("File was modified! Reloading it...")
            scores = json.loads(content)
            scoresText = content
            visitorScore = sum(scores['visitor_scores'])
            homeScore = sum(scores['home_scores'])
            print(scores['at_bat'], scores['inning'])
            print('singles', scores['singles'])
            print('doubles', scores['doubles'])
            print('triples', scores['triples'])
            print('outs', scores['outs'])
            for i in range(scores['inning']):
                print("visitor", i+1, scores['visitor_scores'][i])
                writeScore(i, scores['visitor_scores'][i], 'v')
            print("visitor_total", visitorScore)
            for i in range(scores['inning']):
                print("home", i+1, scores['home_scores'][i])
                writeScore(i, scores['home_scores'][i], 'h')
            writeTotal(visitorScore, 'v')
            writeTotal(homeScore, 'h')
        time.sleep(0.5)

def digitMatrix(n):
    if n % 10 == 0:
    # Do the thing
        return [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    elif n % 10 == 1:
        # Do the other thing
        return [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    elif n % 10 == 2:
        # Do the other thing
        return [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
    elif n % 10 == 3:
        # Do the other thing
        return [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    elif n % 10 == 4:
        # Do the other thing
        return [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
    elif n % 10 == 5:
        # Do the other thing
        return [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    elif n % 10 == 6:
        # Do the other thing
        return [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif n % 10 == 7:
        # Do the other thing
        return [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    elif n % 10 == 8:
        # Do the other thing
        return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif n % 10 == 9:
        # Do the other thing
        return [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
    else:
        # Do the default
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def writeScore(inning, score, team):
    if team == 'v':
        starting_light = 1
    else:
        starting_light = 201
    starting_light = starting_light + ((inning) * 14)
    light_pattern = digitMatrix(score)
    for i in range(13):
        print("Light ", i+starting_light, " ", light_pattern[i])

def writeTotal(score, team):
    if team == 'v':
        starting_light = 127
        print("Visitor Total ", score)
    else:
        starting_light = 327
        print("Home Total ", score)
    if score//10 > 0:
        light_pattern = digitMatrix(score//10)
        for i in range(13):
            print("Light ", i+starting_light, " ", light_pattern[i])
    starting_light = starting_light + 14
    light_pattern = digitMatrix(score)
    for i in range(13):
        print("Light ", i+starting_light, " ", light_pattern[i])




threading.Thread(target=fileWatcher).start()
