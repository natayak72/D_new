from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostCreateForm
# Create your views here.


class NewsInstance(DetailView):
    model = Post
    template_name = 'news/item.html'
    context_object_name = 'news'
    queryset = Post.objects.all()


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


class NewsCreate(ListView):
    model = Post
    template_name = 'news/create.html'
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCreateForm
        return context
