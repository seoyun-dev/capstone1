import json

from django.http            import JsonResponse
from django.views           import View

from users.models     import User

class KakaoSocialLoginView(View):
    def get(self, request):
        try:
            data       = json.loads(request.body)

            user, created = User.objects.get_or_create(
                kakao_id   = data['id'],
                nickname   = data['nickname']
            )

            if created:
                return JsonResponse({"message" : "SIGNUP_SUCCESS"}, status=201)
            
            return JsonResponse({"message" : "LOGIN_SUCCESS"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"message" : "JSONDecodeError"}, status=404)
    
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)