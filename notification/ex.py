from gi.repository import Notify
import time

Notify.init("App Name")
notification = Notify.Notification.new("Hi")
notification.show()
#time.sleep(5)
#notification.close()
#notification = Notify.Notification.new("Hello")
#notification.show()
#time.sleep(5)
#notification.close()
Notify.uninit()
