from django.views.generic import TemplateView

# Create your views here.

class AiConsultingView(TemplateView):
    template_name = 'consulting/ai_consulting.html'