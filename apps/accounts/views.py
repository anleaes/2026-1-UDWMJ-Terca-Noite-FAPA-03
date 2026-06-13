import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            context['erro'] = 'Usuário ou senha inválidos.'
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@csrf_exempt
@require_POST
def api_login(request):
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'error': 'Payload inválido.'}, status=400)

    user = authenticate(
        request,
        username=data.get('username', ''),
        password=data.get('password', ''),
    )
    if user is not None:
        login(request, user)
        return JsonResponse({'ok': True, 'username': user.username, 'is_admin': user.is_staff})
    return JsonResponse({'error': 'Usuário ou senha inválidos.'}, status=401)


def api_me(request):
    if request.user.is_authenticated:
        return JsonResponse({'ok': True, 'username': request.user.username, 'is_admin': request.user.is_staff})
    return JsonResponse({'ok': False}, status=401)


def api_logout(request):
    logout(request)
    return JsonResponse({'ok': True})
