from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout, authenticate

# def login(request):
#     mensaje = ''
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         contrasena  = request.POST.get('pass')
#         user = authenticate(username=username, password=contrasena)
#         #verifica si exite cuenta 
#         if user is not None:
#             if user.is_active:#si esta activo
#                 auth_login(request, user)
#                 return redirect('ticket_app:home_ticket')
#             else:
#                 mensaje = 'USUARIO INACTIVO'
#         else:
#             mensaje = 'USUARIO O CONTRASEÑA INCORRECTOS'
#     return render(request, 'login/login.html', {'mensaje': mensaje})

# #view cierre sesion
# def logout_view(request):
#     logout(request)
#     return redirect('login_app:login')