from django.shortcuts import render
from .models import Password

from rest_framework.response import Response
from api.serializer import PasswordSerializer
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from api.src import generator
import json
import ast

class PasswordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def create_password(request):
    """
    get random password
    """

    try:
        data = json.loads( request.body.decode('utf-8') )
    except KeyError:
      Response("Malformed data!")

    try:
        password = generator.main(
            use_upper = ast.literal_eval(data["use_upper"]),
            use_lower = ast.literal_eval(data["use_lower"]),
            use_digits = ast.literal_eval(data["use_digits"]),
            use_punctuation = ast.literal_eval(data["use_punctuation"]),
            use_space = ast.literal_eval(data["use_space"]),
            additional = data["additional"],
            blacklist = data["blacklist"],
            length = int(data["length"]),
            max_duplicate_chars = int(data["max_duplicate_chars"])
        )
        return Response(password)
    except Exception as e:
        print(e)
        return Response("Try Again!")

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def create_and_save_password(request):
    """
    get random password
    """

    try:
        data = json.loads( request.body.decode('utf-8') )
    except KeyError:
      Response("Malformed data!")

    try:
        password = generator.main(
            use_upper = ast.literal_eval(data["use_upper"]),
            use_lower = ast.literal_eval(data["use_lower"]),
            use_digits = ast.literal_eval(data["use_digits"]),
            use_punctuation = ast.literal_eval(data["use_punctuation"]),
            use_space = ast.literal_eval(data["use_space"]),
            additional = data["additional"],
            blacklist = data["blacklist"],
            length = int(data["length"]),
            max_duplicate_chars = int(data["max_duplicate_chars"])
        )
        Password.objects.create(password=password)
        return Response(password)
    except Exception as e:
        print(e)
        return Response("Try Again!")

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def create_password_with_image(request):
    """
    get random password
    """

    try:
        data = json.loads( request.body.decode('utf-8') )
    except KeyError:
      Response("Malformed data!")

    try:
        password = generator.main(
            use_upper = ast.literal_eval(data["use_upper"]),
            use_lower = ast.literal_eval(data["use_lower"]),
            use_digits = ast.literal_eval(data["use_digits"]),
            use_punctuation = ast.literal_eval(data["use_punctuation"]),
            use_space = ast.literal_eval(data["use_space"]),
            additional = data["additional"],
            blacklist = data["blacklist"],
            length = int(data["length"]),
            max_duplicate_chars = int(data["max_duplicate_chars"])
        )
        image_path = "/app/password_generator/api/static/password.jpg"
        generator.create_image(password,out_path=image_path)

        return FileResponse(open(image_path, 'rb'))

    except Exception as e:
        print(e)
        return Response("Try Again!")

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def create_and_save_password_with_image(request):
    """
    get random password
    """

    try:
        data = json.loads( request.body.decode('utf-8') )
    except KeyError:
      Response("Malformed data!")

    try:
        password = generator.main(
            use_upper = ast.literal_eval(data["use_upper"]),
            use_lower = ast.literal_eval(data["use_lower"]),
            use_digits = ast.literal_eval(data["use_digits"]),
            use_punctuation = ast.literal_eval(data["use_punctuation"]),
            use_space = ast.literal_eval(data["use_space"]),
            additional = data["additional"],
            blacklist = data["blacklist"],
            length = int(data["length"]),
            max_duplicate_chars = int(data["max_duplicate_chars"])
        )
        image_path = "/app/password_generator/api/static/password.jpg"
        generator.create_image(password,out_path=image_path)
        Password.objects.create(password=password)
        return FileResponse(open(image_path, 'rb'))

    except Exception as e:
        print(e)
        return Response("Try Again!")
