
name = "locked"

def doData():
    status = getServerStatus()
    if status["version"] >= "2.2.0":
        ratio = status["globalLock"]["lockTime"] / status["globalLock"]["totalTime"]
    else:
        ratio = status["globalLock"]["ratio"]
    print name + ".value " + str(100 * ratio)

def doConfig():

    print "graph_title MongoDB write lock percentage"
    print "graph_args --base 1000 -l 0 "
    print "graph_vlabel percentage"
    print "graph_category MongoDB"

    print name + ".label " + name





