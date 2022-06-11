from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = "Регистарция"
        return render(request, 'account/sign_up.html', context=data)
    elif request.method == 'POST':
        # 1 - извлечение данных из славаря POST:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # 2 - Техническая проверка:
        data['login'] = login_x
        data['pass1'] = pass1_x
        data['pass2'] = pass2_x
        data['email'] = email_x

        # 3 -  Валидация данных на стороне сервера:
        if pass1_x != pass2_x:
            data['color'] = 'red'
            data['report'] = 'Введенные пороли не совпадают!'
        elif login_x == '...':
            # Остальные проверки
            pass
        else:
            # Регистрация
            user = User.objects.create_user(login_x, email_x, pass1_x)
            user.save()
            if user is None:
                data['color'] = 'red'
                data['report'] = 'В регистрации отказано'
            else:
                data['color'] = 'cadetblue'
                data['report'] = 'Регистарция успешно завершина'
        # Fin - Отправка отчета:
        data['title'] = "Отчёт о регистрации"
        return render(request, 'account/report.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Авторизация'
        return render(request, 'account/sign_in.html', context=data)
    elif request.method == 'POST':
        # 1 Получения данных из формы авторизации:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get("pass1")

        # 2 Проверка подлиности значения логин/пароль:
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            data['color'] = 'red'
            data['report'] = 'Не верный логин или пароль!'
            data['title'] = 'Отчет об авторизации'
            return render(request, 'account/report.html', context=data)
        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    logout(request)
    return redirect('/home')


def profile(request):
    data = dict()
    data['title'] = 'Профиль'
    return render(request, 'account/profile.html', context=data)


def ajax_reg1(request):
    response = dict()
    login_x = request.GET.get('loginX')
    try:
        User.objects.get(username=login_x)
        response['mess'] = 'занят'
    except User.DoesNotExist:
        response['mess'] = 'свободен'

    return JsonResponse(response)


def ajax_reg2(request):
    response = dict()
    email_x = request.GET.get('emailX')
    try:
        User.objects.get(email=email_x)
        response['mess'] = 'занят'
    except User.DoesNotExist:
        response['mess'] = 'свободен'

    return JsonResponse(response)
