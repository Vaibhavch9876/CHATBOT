from django.views.generic import TemplateView, ListView

from .models import Problem
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Problem
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        queries = self.request.GET.get('q')
        # for query in queries.split():
        objects = [
            Problem.objects.filter(Q(p_tags__iregex='\\b(' + query + ')\\b')) for query in list(queries.strip().split())
        ]
        obj_list = []
        for i in objects :
            for j in i:
                obj_list.append(j)
        obj_list = list(set(obj_list))
        print(obj_list)
        return obj_list