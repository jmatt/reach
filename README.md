reach
=====

Python is now reachable. A python library that provides Apple's
objective-c reachability.

Install
-------

```bash
pip install -e git+git://github.com/jmatt/reach.git#egg=reach 
```

Use
---

```python
from Foundation import NSNotificationCenter
from AppKit import NSLog, NSObject, NSWorkspace
from reach.Reachability import Reachability, kReachabilityChangedNotification

reachability = Reachability.new()

class ReachabilityHandler(NSObject):
    """
    Handle reachability notifications from the network.
    """
    def handleChange_(self, notification):
        """
        Handle Reachability changes with the CartelApp.
        """
        NSLog("change!")

rhandler = ReachabilityHandler.new()

workspace = NSWorkspace.sharedWorkspace()
default_center = NSNotificationCenter.defaultCenter()
default_center.addObserver_selector_name_object_(
            rhandler,
            "handleChange:",
            kReachabilityChangedNotification,
            None)
reachability.startNotifier()
```
