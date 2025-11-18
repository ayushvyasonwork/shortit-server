from django.http import JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import ShortURL
import json
import string
import random


def _random_slug(n=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))


@csrf_exempt
def create_short(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('POST only')
    try:
        data = json.loads(request.body.decode())
        target = data.get('target')
        custom = data.get('custom_slug')

        if not target:
            return JsonResponse({'error': 'target required'}, status=400)

        slug = custom or _random_slug()

        # ensure unique slug
        while ShortURL.objects.filter(slug=slug).exists():
            slug = _random_slug()

        obj = ShortURL.objects.create(slug=slug, target=target)

        # DOMAIN FOR SHORT URL — dynamic from settings
        short_host = settings.SHORT_HOST

        short_url = f"https://{short_host}/r/{slug}/"

        return JsonResponse({'short_url': short_url})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def redirect_view(request, slug):
    try:
        obj = ShortURL.objects.get(slug=slug)

        obj.visits += 1
        obj.save()

        redirect = HttpResponseRedirect(obj.target)

        # ⭐ Dynamic custom header, NOT hardcoded
        redirect['X-Short-Domain'] = settings.SHORT_HOST

        return redirect

    except ShortURL.DoesNotExist:
        return JsonResponse({'error': 'not found'}, status=404)
