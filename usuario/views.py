from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from publicacion.models import Publicacion
from .models import Usuario
from .forms import UsuarioForm, LoginForm, NewUser, NewPublicacion
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.

def menu(request):
    context ={
        
    }
    return render(request, 'examples/dashboard.html', context)

def registro_user(request):
    message = 'NOt LOgin'
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = request.POST['username']
            password = request.POST['password']
            print(user, password)
            user = authenticate(username= user, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('usuario:menu')
                    message = 'En curso...'
                   
                else:
                    message = 'Usuario no activo'
            else:
                message = 'Usuario o contraseña incorrecta'
        context ={
        'form': form, 
        'message': message
        }
        
    context ={
        'form': form,
        'message': message
    }
    return render(request, 'login.html', context)


class CrearUsuario( generic.FormView):
    template_name = 'singout.html'
    form_class = NewUser
    success_url = reverse_lazy('usuario:datos_usuario')

    def form_valid(self, form):
        user = form.save()
        return super(CrearUsuario, self).form_valid(form)



class Publicaciones(generic.ListView):
    template_name = 'examples/publicaciones.html'
    model = Publicacion

    def get_queryset(self, *args, **kwargs):
        queryset = Publicacion.objects.filter(user = self.request.user )
        return queryset




class Perfil_user(generic.ListView):
    template_name = 'examples/perfiluser.html'
    model = Usuario
    def get_queryset(self, *args, **kwargs):
        queryset = Usuario.objects.filter(user = self.request.user )
        return queryset
    


def datos_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
            return redirect('usuario:registro_user')
    else:
            form = UsuarioForm()
        
    return render(request, 'datos_usuario.html', {'form':form } )

def crear_publicaciones(request):
    if request.method == 'POST':
        form = NewPublicacion(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('usuario:Publicaciones')

    else:
        form = NewPublicacion()
    
    return render(request, 'examples/crearpublicacion.html', {'form':form } )

class Ver_publicacion(LoginRequiredMixin, generic.DetailView):
    template_name = 'publicacionesuser/verpublicacion.html'
    model = Publicacion



class Eliminar_publicacion(LoginRequiredMixin, generic.DeleteView):
    template_name = 'publicacionesuser/eliminarpublicacion.html'
    model = Publicacion
    success_url = reverse_lazy('usuario:Publicaciones')



class Editar_publicacion(LoginRequiredMixin, generic.UpdateView):
    template_name = 'publicacionesuser/editarpublicacion.html'
    model = Publicacion
    form_class = NewPublicacion
    success_url = reverse_lazy('usuario:Publicaciones')
    