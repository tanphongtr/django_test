from django.http import (
    HttpResponse,
    HttpResponseServerError,
    FileResponse,
)
import datetime

import os
from django.conf import settings
text = open(os.path.join(settings.MEDIA_ROOT, '1.png'), 'rb').read()

# def HomePageViewSet(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def HomePageViewSet(request):
    return HttpResponseServerError()


def FileResponseViewSet(request):
    return FileResponse(open(os.path.join(settings.MEDIA_ROOT, '1.png'), 'rb'))