from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url, redirect
from django.conf import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.is_anonymous and not request.path.startswith('/accounts'):
            return redirect(settings.LOGIN_URL)
        # if request.user.is_anonymous and request.path!=settings.LOGIN_URL:
            # return HttpResponseRedirect(resolve_url('login'))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
