import time
import json
import urllib
import urllib2
import os
import operator

try:
    while True:
        req = urllib2.Request("http://localhost:5000/board", json.dumps({ 'ping_id' : time.time()}), headers={'Content-type': 'application/json', 'Accept': 'application/json'})
        response = urllib2.urlopen(req)
        os.system('clear')
        board = response.read()
        d = json.loads(board)
        #d.sort(key=operator.itemgetter('coins_earned'))
        print "LEADERBOARD"
        print "-----------"
        print "Miner# \t Coins Earned"
        for i in d:
            print str(d[i]['miner_address']) + "\t\t" + str(d[i]['coins_earned']) + " ",
            for x in range(0, d[i]['coins_earned']):
                print u"\u2588",
            print " "
        time.sleep(5) 
except KeyboardInterrupt:
    print('interrupted!')