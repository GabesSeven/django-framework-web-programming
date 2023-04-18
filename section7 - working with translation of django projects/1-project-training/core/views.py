from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Caracteristica
from .forms import ContatoForm

from django.utils.translation import gettext as _
from django.utils import translation

# Create your views here.
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionario'] = Funcionario.objects.order_by('?').all()
        caracteristicas = Caracteristica.objects.order_by('?').all()
        size = int(len(caracteristicas) / 2)
        context['caracteristicas_esquerda'], context['caracteristicas_direita'] = caracteristicas[:size], caracteristicas[size:]
        context['lang'] = lang
        translation.activate(lang)

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso.'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail.'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)





# Django automatically recognizes error pages
# if there is a 404.html file or other error in templates
# class TesteView(TemplateView):
    # template_name = '404.html'

# class TesteTwoView(TemplateView):
    # template_name = '500.html'
