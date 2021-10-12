from gi.repository import Notify
Notify.init("Test App")

msg = ''' jahkfasdhf\
sdfkafkjdf \ 
kfda
kadfafjadsgfkaudfgjksadgkfu\
'''


# A raw file name/path
Notify.Notification.new(
    "Ding!",
    msg,
    "/home/KEERTHANA/cricket_score/Desert.jpg"
).show()

# Or a icon name in the theme
Notify.Notification.new(
    "Ding!",
    "Time is up.",
    "dialog-information" # dialog-warn, dialog-error
).show()
