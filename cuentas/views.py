from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView, UpdateView
from cuentas.models import Usuarios, Dispositivos, Alarma
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_exempt

class LoginDir(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = "home.html"
    success_url = reverse_lazy("cuenta:home")
    success_message = "Welcome back %(username)s!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print(True)
            return redirect(self.get_success_url())
        else:
            print(False)
            return super(LoginDir, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginDir, self).form_valid(form)

class geta(CreateView):
    model = Usuarios
    fields = ['usr2']
    print("hola mundo")

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(geta, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST['fecha']
        print(1234)
        print(data)
