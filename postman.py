#!/usr/bin/env python

import sys, os, time, requests
from daemon import Daemon
    
class PostMan(Daemon):
    def __init__(self, pidfile):
        super(PostMan, self).__init__(pidfile)
        self.url = 'http://api.oakridge.io/redirector/v1/version/control?key=1'
    def query(self):
        return requests.get(self.url, params={}, json={})
    def run(self):
        while True:
            time.sleep(1)
            res = self.query()
            print res.status_code
            
if __name__ == "__main__":
    daemon = PostMan('/tmp/daemon-postman.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'Start' == sys.argv[1]:
            daemon.Start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
            sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

