import time

from pip._internal.vcs import git
from plyer import notification

while(True):
    notification.notify(
        title = "bilgisayara biraz ara ver",
        message = "kendin için birşeyler yap",
        timeout = 90
    )

    time.sleep(90*90)

   