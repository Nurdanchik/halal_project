from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

class TestCacheView(APIView):
    def get(self, request):
        value = cache.get('my_key')
        if value is None:
            cache.set('my_key', 'Hello from Redis!', timeout=60)  # 1 минута
            value = 'Set new value in Redis'
        return Response({"message": value})