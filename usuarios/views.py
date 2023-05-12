from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from multiprocessing import context
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.views.generic import View 
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm ,PasswordResetForm
from django.contrib import messages
from django.core.mail import EmailMessage
from usuarios.forms import FormularioContacto, emailform 
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy 
from django.http import HttpResponseRedirect


# Create your views here.

class email(TemplateView, FormView):
    template_name = 'usuarios/correo.html'
    form_class = emailform
    success_url = reverse_lazy('correo')

    def post(self, request):
        form = emailform(request.POST)

        if form.is_valid():

            nombre = request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            send_mail(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(
                    nombre, email, message),
                email,
                ['milimo1230@gmail.com'],
                fail_silently=False,
            )
            try:
                return HttpResponseRedirect(self.success_url, messages.success(self.request, f'se envio el mensaje'))
            except:
                # Ha habido un error y retorno a ERROR
                return HttpResponseRedirect(self.success_url, messages.error(self.request, f'No se envio el mensaje'))
        return render(request, self.template_name, {'form': form})




def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")


            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["aquí la dirección del destinatario"],reply_to=[email])
            
            try:
                email.send()
               
                return redirect("/usuarios/contacto/?valido")
            except:
                return redirect("/usuarios/contacto/?novalido")


    return render(request, "usuarios/contacto.html", {'miFormulario':formulario_contacto})


class VRegistro(View):

    def get(self, request):
        form=SignUpForm( )
        return render(request,"usuarios/registro.html",{"form":form})

    def post(self, request):
        form=SignUpForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request, usuario)

            return redirect('inicio')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"usuarios/registro.html",{"form":form})



def usuarios(request):
    context = {
        
    }
    return render(request, 'usuarios/usuarios.html', context)

def somos(request):        
    return render(request, "partials/somos.html")

def login_view(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('Tienda')
          
    
    return render(request, 'usuarios/login.html', {
        
    })
    
def logout_view(reques):
    logout(reques)
    messages.success(reques, 'Sesión cerrada exitosamente')
    return redirect('login')
