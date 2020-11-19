from django.views.generic import TemplateView

# Create your views here.


class LectureView(TemplateView):
    template_name = 'lecture/lecture.html'
