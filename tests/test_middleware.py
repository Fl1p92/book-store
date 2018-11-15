from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.shortcuts import reverse

from apps.core.models import Request
from apps.core.middleware import SaveRequestMiddleware
from apps.store.views import HomeView


class SaveRequestMiddlewareTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_save_request_middleware(self):
        self.assertEqual(Request.objects.count(), 0)

        request = self.factory.get(reverse("store:index"))
        request.user = AnonymousUser()
        middleware = SaveRequestMiddleware(get_response=HomeView.as_view())
        response = middleware(request)
        request_object = Request.objects.first()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Request.objects.count(), 1)
        self.assertEqual(str(request.user), request_object.user)
        self.assertEqual(request.path, request_object.path)
