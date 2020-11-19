from django.views.generic import TemplateView, ListView, DetailView
from academy.models import Level, Contents

# Create your views here.


class LevelLV(ListView):
    model = Level


class ContentsDV(DetailView):
    model = Contents


class AcademyClassView(TemplateView):
    template_name = 'academy/academy_class.html'


class IntroduceView(TemplateView):
    template_name = 'academy/introduce.html'


class MathClassView(TemplateView):
    template_name = 'academy/math_class.html'


class BeginnerView(TemplateView):
    template_name = 'academy/introduce_beginner.html'


class MiddleView(TemplateView):
    template_name = 'academy/introduce_middle.html'


class MachineLearningView(TemplateView):
    template_name = 'academy/machineLearning.html'


class ComputerVisionView(TemplateView):
    template_name = 'academy/computerVision.html'

class NlpView(TemplateView):
    template_name = 'academy/nlp_class.html'
