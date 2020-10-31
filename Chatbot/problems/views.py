from django.views.generic import TemplateView, ListView

from .models import Problem
from django.db.models import Q

## EXTRACT SKILL-TAGS FROM USER INPUT ---------------------------------------------------------------------------------------
import json

first_time = True
JSON_SKILL_LIST_PATH = "skillList.json"
skill_file_obj = None
skill_list = {}
space_added_skill_list = {}


def loadSkillList():
    global skill_list
    global skill_file_obj
    global space_added_skill_list
    # skill_file_obj = open(JSON_SKILL_LIST_PATH , )
    # skill_list = json.load(skill_file_obj)
    skill_list = {
        "c" : ["c"] ,
        "cpp": ["c++", "cplusplus"],
        "java": ["java", "java8", "JavaC"],
        "c#": ["csharp", "chash", "c#"],
        "python" : ["python" , "python3" , "python2" , "py"] ,
        "numpy" : ["numpy" , "np" , "python" , "python2" , "python3" , "python2"] ,
        "scipy" : ["scipy"] ,
        "sklearn" : ["scikit-learn" , "sklearn" , "sk learn"] ,
        "tensorflow" : ['tensorflow', 'tf', 'tensor-flow'] ,
        "keras" : ["keras"] ,
        "h20" : ["h20"] ,
        "PHP" : ["php"] ,
        "SQl" : ["SQL" , "mysql" , "Postgress", "Postgresql" , "Oracle"] ,
        "R" : ["R"] ,
        "javascript": ["js", "js6", "javascript", "javaScript6"]
    }
    for skill in skill_list:
        space_added_skill_list[skill] = [' ' + skill_alias + ' ' for skill_alias in skill_list[skill]]
    print("Loaded Skill List", skill_list)
    print("Space Added Skill List", space_added_skill_list)


def findSkills(i_text):
    space_added_text = ' ' + i_text + ' '
    found_skills = {}
    for skill in space_added_skill_list:
        skill_count = 0
        for space_added_skill_alias in space_added_skill_list[skill]:
            skill_count += space_added_text.count(space_added_skill_alias)
        if skill_count > 0:
            found_skills[skill] = skill_count
    print("Skills Found : ", found_skills)
    return found_skills


###EXTRACTION ENDS HERE---------------------------------------------------------------------------------------------------------------

class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Problem
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        global first_time
        query_text = self.request.GET.get('q')
        skill_count = {}
        if first_time:
            loadSkillList()
            first_time = False
        skill_count = findSkills(query_text)
        print("FOUND SKILLCOUNT " , skill_count )
        queries = ""
        for skill in skill_count:
            queries += " " + skill
        # queries = self.request.GET.get('q')
        # for query in queries.split():
        objects = [
            Problem.objects.filter(Q(p_tags__iregex='\\b(' + query + ')\\b')) for query in list(queries.strip().split())
        ]
        obj_list = []
        for i in objects:
            for j in i:
                obj_list.append(j)
        obj_list = list(set(obj_list))
        print(obj_list)
        return obj_list
