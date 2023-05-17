# import json

# from django.http        import JsonResponse
# from users.models       import User
# from capstone1.settings import SECRET_KEY

# def signin_decorator():
#     def wrapper(self, request):
#         try:
#             user_token = request.headers.get('Authorization', None)
#             payload = jwt.decode(user_token, SECRET_KEY, algorithm='HS256')
#             request.user = User.objects.get(id=payload['id'])
#             data         = json.loads(request.body)
#             user         = User.objects.get(kakao_id = data['id'])
#             request.user = user

#             return JsonResponse({'message':'LOGIN_USER'}, status=200)

#         except User.DoesNotExist:
#             return JsonResponse({'message':'INVALID_USER'}, status=400)

#         except json.JSONDecodeError:
#             return JsonResponse({"message" : "JSONDecodeError"}, status=404)

#     return wrapper