
def get():
    return getServerStatus()["metrics"]["document"]


def doData():
    for k, v in get().iteritems():
        print( str(k) + ".value " + str(v) )

def doConfig():

    print "graph_title MongoDB documents"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel documents"
    print "graph_category MongoDB"

    for k in get():
        print k + ".label " + k
        print k + ".min 0"
        print k + ".type COUNTER"
        print k + ".max 500000"
        print k + ".draw LINE1"




