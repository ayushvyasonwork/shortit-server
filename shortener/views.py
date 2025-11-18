from django.http import JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import ShortURL
import json, string, random
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
            return JsonResponse({'error':'target required'}, status=400)
        slug = custom or _random_slug()
        # ensure unique
        while ShortURL.objects.filter(slug=slug).exists():
            slug = _random_slug()
        obj = ShortURL.objects.create(slug=slug, target=target)
        short_host = 'localhost:8000'

        short_url = f"http://{short_host}/r/{slug}/"
        return JsonResponse({'short_url': short_url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def redirect_view(request, slug):
    try:
        obj = ShortURL.objects.get(slug=slug)
        obj.visits += 1
        obj.save()
        redirect = HttpResponseRedirect(obj.target)
        # Add the custom header required by the user
        redirect['X-Short-Domain'] = 'shortit.projects.ayushvyas.me'
        return redirect
    except ShortURL.DoesNotExist:
        return JsonResponse({'error':'not found'}, status=404)
