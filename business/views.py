from django.views.generic import TemplateView

# Create your views here.


class BusinessView(TemplateView):
    template_name = 'business/business.html'
