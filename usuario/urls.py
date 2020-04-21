from django.urls import path, include
from usuario import views

app_name  = 'usuario'
urlpatterns = [
    path('', views.registro_user, name='registro_user'), 
    path('menu/', views.menu, name='menu'),
    path('datos_usuario/', views.datos_usuario, name='datos_usuario'),
    path('CrearUsuario/', views.CrearUsuario.as_view(), name="CrearUsuario"),
    path('Publicaciones/', views.Publicaciones.as_view(), name="Publicaciones"),
    path('Perfil_user/', views.Perfil_user.as_view(), name="Perfil_user"),
    path('crear_publicaciones/', views.crear_publicaciones, name="Crear_publicaciones"),

]