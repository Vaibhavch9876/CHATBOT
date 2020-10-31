from django.views.generic import TemplateView, ListView

from .models import Problem
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Problem
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Problem.objects.filter(
            Q(p_tags__icontains=query)
        )
        return object_list