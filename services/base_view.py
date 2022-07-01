import functools
from django.shortcuts import render
import logging

logger = logging.getLogger("app")


def base_view(fn):
    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            return fn(request, *args, **kwargs)
        except Exception as ex:
            logger.error(ex)
            return render(request, "error.html", {"message": str(ex)}, status=400)

    return inner
