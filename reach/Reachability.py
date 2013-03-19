"""
Python is now reachable. A python library that provides Apple's
objective-c reachability.

Author: J. Matt Peterson

Source: https://github.com/jmatt/reach

See: http://developer.apple.com/library/ios/#samplecode\
...  /Reachability/Listings/Classes_Reachability_m.html

"""
from AppKit import NSObject, NSLog, NSWorkspace
from Foundation import NSNotificationCenter, NSDistributedNotificationCenter
from PyObjCTools import AppHelper
from SystemConfiguration import CFRunLoopGetCurrent, kCFRunLoopCommonModes,\
    kCFRunLoopDefaultMode, kSCNetworkFlagsInterventionRequired,\
    SCNetworkReachabilityCreateWithAddress, SCNetworkReachabilityGetFlags,\
    SCNetworkReachabilityScheduleWithRunLoop,\
    SCNetworkReachabilityUnscheduleFromRunLoop,\
    SCNetworkReachabilitySetCallback


INET_ADDR = "8.8.8.8"
kReachabilityChangedNotification = "kNetworkReachabilityChangedNotification"


use_distributed = False


def reachabilityCallback(target, flags, info):
    """
    Default reachabilityCallback.

    Log flags and post notification to the defaultCenter of
    NSNotificationCenter.

    Note: that if this event is not used
    then the developer must post notification or the
    kReachabilityChangedNotification will not happen.
    """
    NSLog("reachability!")
    NSLog("flags = %s" % str(flags))
    NSLog("kSCNetworkFlagsInterventionRequired = %s"
          % (flags & kSCNetworkFlagsInterventionRequired))
    note = None
    if use_distributed:
        note = NSDistributedNotificationCenter.defaultCenter()
    else:
        note = NSNotificationCenter.defaultCenter()
    note.postNotificationName_object_(kReachabilityChangedNotification, info)


class Reachability(object):
    """
    Handle reachability notifications from the network.
    """

    def startNotifier(self, callback=reachabilityCallback, distributed=False):
        """
        Start notifications with callback.

        By default use reachabilityCallback which will fire a
        kReachabilityChangedNotification event using the defined variable.
        """
        global use_distributed
        use_distributed = distributed

        self.loop = CFRunLoopGetCurrent()

        self.target = SCNetworkReachabilityCreateWithAddress(None,
                                                             (INET_ADDR, 80))
        SCNetworkReachabilitySetCallback(self.target,
                                         callback,
                                         INET_ADDR)

        ok, flags = SCNetworkReachabilityGetFlags(self.target, None)

        if ok:
            callback(self.target, flags, INET_ADDR)

        SCNetworkReachabilityScheduleWithRunLoop(
            self.target,
            self.loop,
            kCFRunLoopCommonModes)

    def stopNotifier(self):
        """
        Stop notifications.
        """
        self.loop = CFRunLoopGetCurrent()
        SCNetworkReachabilityUnscheduleFromRunLoop(
            self.target,
            self.loop,
            kCFRunLoopDefaultMode)


def main():
    reachability = Reachability()
    reachability.startNotifier(distributed=True)
    AppHelper.runConsoleEventLoop(installInterrupt=True)


if __name__ == "__main__":
    main()
