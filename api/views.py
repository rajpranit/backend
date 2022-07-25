from django.http import JsonResponse


def ApiHome(request, *args, **kwargs):

    body = request.body
    print(body)
    return JsonResponse({"message": "hi there this is your json api response"})
