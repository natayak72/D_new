from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
# Create your views here.


class NewsList(ListView):
    model = Post
    template_name = 'news/list.html'
    context_object_name = 'news_list'
    allow_empty = True  # Возвращает пустой список, если объектов нет (если False - будет 404)
    ordering = ['-create_datetime']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())

        return context


