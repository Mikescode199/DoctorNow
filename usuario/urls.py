from django.urls import path, include
from usuario import views
from componente.class_views import Menu

app_name  = 'usuario'
urlpatterns = [
    path('', views.registro_user, name='registro_user'), 
    path('menu/', Menu.as_view(), name='menu'),
    path('logout_usuario/', views.logout_usuario, name='logout_usuario'),
    path('datos_usuario/', views.datos_usuario, name='datos_usuario'),
    path('CrearUsuario/', views.CrearUsuario.as_view(), name="CrearUsuario"),
    path('Publicaciones/', views.Publicaciones.as_view(), name="Publicaciones"),
    path('Perfil_user/', views.Perfil_user.as_view(), name="Perfil_user"),
    path('crear_publicaciones/', views.crear_publicaciones, name="Crear_publicaciones"),
    path('Ver_publicacion/<int:pk>', views.Ver_publicacion.as_view(), name='Ver_publicacion'),
    path('Eliminar_publicacion/<int:pk>', views.Eliminar_publicacion.as_view(), name='Eliminar_publicacion'),
    path('Editar_publicacion/<int:pk>', views.Editar_publicacion.as_view(), name='Editar_publicacion'),

    # URL PARA COMPONENTES

]