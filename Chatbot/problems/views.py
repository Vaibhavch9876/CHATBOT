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
        "c": ["c"],
        "cpp": ["c++", "cplusplus"],
        "java": ["java", "java8", "JavaC"],
        "c#": ["csharp", "chash", "c#"],
        "pyth": ["python", "python3", "python2", "py"],
        "numpy": ["numpy", "np"],
        "scipy": ["scipy"],
        "sklearn": ["scikit-learn", "sklearn", "sk learn"],
        "tensorflow": ['tensorflow', 'tf', 'tensor-flow'],
        "keras": ["keras"],
        "h20": ["h20"],
        "PHP": ["php"],
        "SQl": ["SQL", "mysql", "Postgress", "Postgresql", "Oracle"],
        "R": ["R"],
        "javascript": ["js", "js6", "javascript", "javaScript6"]
    }
    for skill in skill_list:
        space_added_skill_list[skill] = [' ' + skill_alias + ' ' for skill_alias in skill_list[skill]]
    print("Loaded Skill List", skill_list)
    print("Space Added Skill List", space_added_skill_list)


def findSkills(i_text):
    global user_tag_str
    space_added_text = ' ' + i_text + ' '
    found_skills = {}
    for skill in space_added_skill_list:
        skill_count = 0
        for space_added_skill_alias in space_added_skill_list[skill]:
            skill_count += space_added_text.count(space_added_skill_alias)
        if skill_count > 0:
            found_skills[skill] = skill_count
    print("Skills Found : ", found_skills)
    for skill in found_skills :
        user_tag_str += " " + skill
    return found_skills


###EXTRACTION ENDS HERE---------------------------------------------------------------------------------------------------------------
import random

MAX_PROBLEMS = 9
problem_displayed = False
problems_that_match_user = {}
lastProblem = -1
problems_asked = []
user_scores = []
user_rating = 0
user_tag_str = ""
SESSION_TERMINATED = False
SKIP_ONE_DONE = False
ALL_QUERY_LIST = []
PREVIOUSLY_RENDERED = {"p_statement" : "HelloWorld! :D"}

def Reset():
    global PREVIOUSLY_RENDERED
    PREVIOUSLY_RENDERED = {"p_statement" : "HelloWorld! :D"}
    global ALL_QUERY_LIST
    ALL_QUERY_LIST = []
    # Reset to default
    global first_time
    first_time = True
    global JSON_SKILL_LIST_PATH
    JSON_SKILL_LIST_PATH = "skillList.json"
    global skill_file_obj
    skill_file_obj = None
    global skill_list
    skill_list = {}
    global space_added_skill_list
    space_added_skill_list = {}
    global user_tag_str
    user_tag_str = ""

    global MAX_PROBLEMS
    MAX_PROBLEMS = 9
    global problem_displayed
    problem_displayed = False
    global problems_that_match_user
    problems_that_match_user = {}
    global lastProblem
    lastProblem = -1
    global problems_asked
    problems_asked = []
    global user_scores
    user_scores = []
    global user_rating
    user_rating = []
    global SESSION_TERMINATED
    SESSION_TERMINATED = False
    global SKIP_ONE_DONE
    SKIP_ONE_DONE = False

def generateReport():
    SESSION_TERMINATED = True
    """
    Message!
    Scored : __ of __ 
    Percentile Score : ___
    Remarks : About practicing weak topics and 
    Enter your email to receive these problems with solutions on your email
    """

    # Generate Dummy Data for generating a realistic report
    # This can be added to database and later used for other users

    skill_set_max_rating = int(random.randrange(20 , 30) * 100)
    user_percentile_score = round(((user_rating * 100) / skill_set_max_rating) + random.randrange(-5 , 5) , 3)
    user_percentile_score = min(user_percentile_score , 99.999 )
    user_percentile_score = max(user_percentile_score , 1)

    user_report = {
        "p_statement" : "Congratulations on completing this quiz!!" ,
        "p_A" : "You scored " + str(user_scores.count(1)) + " of " + str(len(user_scores)) ,
        "p_B" : "You reached a final rating of " + str(user_rating) + " of " + str(skill_set_max_rating) ,
        "p_C" : "Your Percentile score was " + str(user_percentile_score) ,
        "p_D" : "Great! You are pretty good at " + user_tag_str ,
        "p_E" : "Enter your email to get detailed solutions to the problems, or refer them later! :D"
    }
    if user_percentile_score > 75 :
        user_report["p_D"] = "Wow! You are pretty good at " + user_tag_str
    elif  user_percentile_score > 50 :
        user_report["p_D"] = "Great! A bit of practice and you will do wonders! in " + user_tag_str
    elif user_percentile_score > 25 :
        user_report["p_D"] = "Consider " + user_tag_str + " in your weak topics for now, but with practice you will ace it"
    else :
        user_report["p_D"] = "You are too weak at " + user_tag_str + ", consider going through the basics again!!"
        # print("USER RATING : " , user_rating)
    # print("PROBLEMS ASKED " , len(problems_asked))
    # print("USER SCORE" , user_scores.count(1))
    # print(problems_asked)
    # print(user_scores)
    return user_report
    # return {"p_statement": "Thankyou for taking the test! :D"}


def evaluateResult(query_text):
    global problem_displayed
    global problems_asked
    global user_rating
    global user_scores
    global problems_asked
    global lastProblem
    problems_asked.append(lastProblem.p_id)
    print("Acc to me LAST PROBLEM WAS " , lastProblem.p_statement)
    if str(query_text).lower() == str(lastProblem.p_correct).lower():
        user_scores.append(1)
        user_rating += 50
    else:
        user_scores.append(-1)
    problem_displayed = True


def giveProblem():
    global user_rating
    global SKIP_ONE_DONE
    global problems_that_match_user
    global lastProblem
    global problem_displayed
    print("user problems , scores " , problems_asked , user_scores)
    if len(problems_asked) > MAX_PROBLEMS:
        return generateReport()
    if len(problems_that_match_user) == 0:
        if SKIP_ONE_DONE :
            return generateReport()
        else :
            SKIP_ONE_DONE = True
            return {'p_statement' : "Hello World!"}
    print("Inside give Problem ")
    while user_rating <= list(problems_that_match_user.keys())[-1]:
        if user_rating in problems_that_match_user:
            if len(problems_that_match_user[user_rating]) == 0:
                user_rating += 50
            else:
                break
        else:
            user_rating += 50

    if user_rating > list(problems_that_match_user.keys())[-1]:
        return generateReport()

    p_index = random.randrange(len(problems_that_match_user[user_rating]))
    lastProblem = problems_that_match_user[user_rating][p_index]
    problems_that_match_user[user_rating] = problems_that_match_user[user_rating][:p_index] + problems_that_match_user[
                                                                                                  user_rating][
                                                                                              p_index + 1:]
    # problems_asked.append(lastProblem.p_id)
    problem_displayed = True
    # print("Chosen problem " , lastProblem)
    return lastProblem


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Problem
    template_name = 'home.html'

    def get_queryset(self):  # new
        global PREVIOUSLY_RENDERED
        global ALL_QUERY_LIST
        global problem_displayed
        global first_time
        global problems_that_match_user
        query_text = self.request.GET.get('q')
        ALL_QUERY_LIST.append(query_text)
        print(len(ALL_QUERY_LIST) , ALL_QUERY_LIST)

        if SESSION_TERMINATED:
            Reset()
        if problem_displayed:
            evaluateResult(query_text)
        if SKIP_ONE_DONE and first_time:
            loadSkillList()
            first_time = False
            print("QUERY RECEIVED ", query_text)
            skill_count = {}

            skill_count = findSkills(query_text)
            print("FOUND SKILLCOUNT ", skill_count)
            queries = ""
            for skill in skill_count:
                queries += " " + skill
            # queries = self.request.GET.get('q')
            # for query in queries.split():
            objects = [
                Problem.objects.filter(Q(p_tags__iregex='\\b(' + query + ')\\b')) for query in
                list(queries.strip().split())
            ]
            obj_list = []
            for i in objects:
                for j in i:
                    obj_list.append(j)
            obj_list = list(set(obj_list))

            obj_dict = {}
            for obj in obj_list:
                if obj.get_rating() not in obj_dict:
                    obj_dict[obj.get_rating()] = list()
                obj_dict[obj.get_rating()].append(obj)

            obj_dict = dict(sorted(obj_dict.items(), key=lambda kv: kv[0]))
            problems_that_match_user = obj_dict
            print(problems_that_match_user)

        # if len(ALL_QUERY_LIST) > 1 and ALL_QUERY_LIST[-1] == ALL_QUERY_LIST[-2]:
        #     print("here " , ALL_QUERY_LIST)
        #     return [PREVIOUSLY_RENDERED]
        PREVIOUSLY_RENDERED = [giveProblem()]
        return PREVIOUSLY_RENDERED
