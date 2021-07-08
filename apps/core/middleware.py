from django.utils.deprecation import MiddlewareMixin

from .models import Request


class SaveRequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        Request.objects.create(
            path=request.path,
            body=request.body,
            method=request.method,
            user=request.user,
        )
