from secrets import token_hex
from django.http import JsonResponse
from rest_framework import views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import AppSerializer
from .models import App


class AppView(views.APIView):
    permission_classes = [AllowAny]
    # queryset = Rating.objects.all()

    def get(self, request):
        response = {}
        response['data'] = {}
        response['success'] = False
        api_key = request.GET.get('api_key')

        if not api_key:
            response['error'] = 'API_KEY is not set'
            return JsonResponse(response)

        try:
            app = App.objects.get(
                api_key=api_key
            )
        except App.DoesNotExist:
            response['error'] = 'API_KEY is not valid'
            return JsonResponse(response)

        response['success'] = True

        serializer = AppSerializer(app)
        response['data'] = serializer.data

        return JsonResponse(response)

    def post(self, request):
        response = {}
        response['success'] = False

        name = request.data.get('name')
        api_key = str(token_hex(32))

        if not name:
            response['error'] = 'name is not set'
            return JsonResponse(response)

        App.objects.create(name=name, api_key=api_key)
        response['success'] = True
        response['API_KEY'] = api_key

        return JsonResponse(response)

    def put(self, request):
        response = {}
        response['success'] = False

        name = request.data.get('name')
        api_key = request.data.get('API_KEY')

        if not name or not api_key:
            response['error'] = 'name or API_KEY is not set'

        try:
            app = App.objects.get(
                api_key=api_key
            )
        except App.DoesNotExist:
            response['error'] = 'API_KEY is not valid'
            return JsonResponse(response)

        app.name = name
        app.save()
        response['success'] = True

        return JsonResponse(response)

    def delete(self, request):
        response = {}
        response['success'] = False

        api_key = request.data.get('API_KEY')

        if not api_key:
            response['error'] = 'API_KEY is not set'

        try:
            app = App.objects.get(
                api_key=api_key
            )
        except App.DoesNotExist:
            response['error'] = 'API_KEY is not valid'
            return JsonResponse(response)

        app.delete()
        response['success'] = True

        return JsonResponse(response)


@api_view(["POST"])
@permission_classes((AllowAny,))
def set_api_key(request):
    response = {}
    response['success'] = False

    api_key = request.data.get('API_KEY')

    if not api_key:
        response['error'] = 'API_KEY is not set'

    try:
        app = App.objects.get(
            api_key=api_key
        )
    except App.DoesNotExist:
        response['error'] = 'API_KEY is not valid'
        return JsonResponse(response)

    app.api_key = str(token_hex(32))
    app.save()
    response['API_KEY'] = app.api_key
    response['success'] = True

    return JsonResponse(response)
