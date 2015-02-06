from django.views.generic import ListView, DetailView
from .models import Entry


class BlogIndexView(ListView):
    queryset = Entry.objects.published()
    template_name = "blog/home.html"
    paginate_by = 4


class BlogDetailView(DetailView):
    model = Entry
    template_name = "blog/post.html"
