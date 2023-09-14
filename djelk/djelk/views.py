from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)


def my_view(request):
    logger.debug("Hi, i'm be pushed to kibana")
    return HttpResponse("Hello, this is the 'foo' view asdasd.")
