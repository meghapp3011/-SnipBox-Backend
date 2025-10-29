from http import HTTPStatus
from rest_framework.exceptions import APIException
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from urllib.parse import urlparse, urlunparse


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']

        status_code = response.status_code

        message = getattr(
            response,
            'custom_message',
            HTTPStatus(status_code).phrase
        )

        if status_code < 400:
            success = True
            data_key = 'data'
        else:
            success = False
            data_key = 'error'

        keys = ["status", "data", "next", "previous"]

        if isinstance(data, dict) and data.keys() and all(
            key in data.keys() for key in keys
        ):
            """
            pagination response
            """
            result = data
        else:
            """
            object response
            """
            result = {
                'success': success,
                'status': status_code,
                'message': message,
                data_key: data,
            }
        return super().render(result, accepted_media_type, renderer_context)


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = None

    def get_paginated_response(self, data):
        status_code = 200
        message = "OK"

        return Response({
            'success': True,
            'status': status_code,
            'message': message,
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            "team_name": getattr(self, 'team_name', None),
            'data': data,
        }, status=status_code)

    def get_next_link(self):
        if not self.page.has_next():
            return None

        url = self.request.build_absolute_uri()
        page_number = self.page.next_page_number()
        next_url = f'{url}&page={page_number}'

        # remove base url
        return self.remove_base_url(next_url)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None

        url = self.request.build_absolute_uri()
        page_number = self.page.previous_page_number()

        if page_number == 1:
            prev_url = url.rsplit('?', 1)[0]
        else:
            prev_url = f'{url}&page={page_number}'

        # remove base url
        return self.remove_base_url(prev_url)

        # convert http to https
        # return self.update_scheme(prev_url, 'https')

    def update_scheme(self, url, new_scheme):
        # Update the URL scheme to 'https'
        parsed_url = urlparse(url)
        updated_url = urlunparse((new_scheme,) + parsed_url[1:])
        return updated_url

    def remove_base_url(self, url):
        # Remove the base URL, keeping only the path and query string
        parsed_url = urlparse(url)
        return urlunparse(('',
                           '',
                           parsed_url.path,
                           parsed_url.params,
                           parsed_url.query,
                           parsed_url.fragment))


class CustomAPIException(APIException):
    """
    to raise custom exception
    """
    status_code = 400

    def __init__(self, detail=None, field=None):
        if detail is not None:
            self.detail = {'detail': detail}
        if field is not None:
            self.detail['field'] = field

    def to_representation(self, instance):
        if isinstance(instance, CustomAPIException):
            # Customize the response for validation errors
            return {
                "success": False,
                "status": instance.status_code,
                "message": "Bad Request",
                "error": {
                    "detail": instance.detail.get('message')
                }
            }
        return super().to_representation(instance)


class ExceptionHandlerMiddleware(MiddlewareMixin):
    """
    all unknown error responses
    """

    def process_exception(self, request, exception):

        data = {
            'success': False,
            'status': '',
            'message': '',
            'error': {
                'detail': str(exception)
            },
        }
        if hasattr(exception, 'status_code'):
            status = exception.status_code
        else:
            status = 500
        data['status'] = status
        data['message'] = HTTPStatus(status).phrase
        response = JsonResponse(data=data, status=status)
        return response
