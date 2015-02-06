from django.views.generic import ListView
from .models import Entry


class BlogIndexView(ListView):
    queryset = Entry.objects.published()
    template_name = "blog/home.html"
    paginate_by = 4
