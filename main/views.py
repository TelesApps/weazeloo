from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Bookmark
from .serializers import BookmarkSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def bookmarks(request):
    bookmarks = Bookmark.objects.all()
    serializer = BookmarkSerializer(bookmarks, many=True)
    return Response(serializer.data)


def dynamic(request, dynamic_value):
    # if dynamic value is a number return the value
    if dynamic_value.isdigit():
        return render(request, "main/main.html", {
            "title": "Dynamic Page",
            "content": f"This is the dynamic page content with value {dynamic_value}"
        })
        return HttpResponse(f"Hello, world. You're at the main dynamic page with value {dynamic_value}.")
    else:
        redirect = reverse("dynamic", args=[dynamic_value])
        return HttpResponseRedirect("/app/home")
