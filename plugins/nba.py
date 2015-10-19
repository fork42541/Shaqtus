import json
import urllib2
from util import hook

@hook.regex("\.nba")
def getGames(match):

    response = urllib2.urlopen('https://api.ballstreams.com/Scores?key=c4699e2020b2b5642485ed44fddd39a1')

    data = json.load(response)
    output = "| "
    for i in range(len(data['scores'])):
        if data['scores'][i]['shortHomeTeam'] == None:
            continue

        home = data['scores'][i]['shortHomeTeam']
        hscore = data['scores'][i]['homeScore']
        away = data['scores'][i]['shortAwayTeam']
        ascore = data['scores'][i]['awayScore']
        if ascore > hscore:
            ascore = '\x02' + ascore + '\x02'
        elif hscore > ascore:
            hscore = '\x02' + hscore + '\x02'
        time = data['scores'][i]['period']
        if data['scores'][i]['isPlaying'] == 0 and time != "Final":
            output += away + ' @ ' + home + ' ' + time + ' | '
        else:
            output += away + ' ' + ascore + ' @ ' + home + ' ' + hscore + ' ' + time + ' | '
    return output
