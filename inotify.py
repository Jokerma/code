import pyinotify
import os
import sys
class WatchLogProceesing(pyinotify.ProcessEvent):
    def process_IN_MOVED_FROM(self, event):
        print "processing %s" % (event.pathname)
    def process_IN_MOVED_TO(self, event):
        print "processing %s" % (event.pathname)
    def process_IN_MOVED_SELF(self, event):
        print "processing %s" % (event.pathname)

def monitor_dir(directory):
    wmn = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wmn, WatchLogProceesing())
    wmn.add_watch(directory, pyinotify.IN_MOVED_FROM)
    wmn.add_watch(directory, pyinotify.IN_MOVED_TO)
    wmn.add_watch(directory, pyinotify.IN_MOVE_SELF)
    notifier.loop()

monitor_dir("./a")
