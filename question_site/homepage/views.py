from django.shortcuts import render
from stacked.models import Question
from stacked.forms.question_form import QuestionForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from accounts.models import UserScore

#search stuff
import operator
from django.db.models import Q
from stacked.views import QuestionList


# Takes the users to the homepage
def index(request):

    if request.method == 'GET':
        form = QuestionForm()
    else:
        # take in the form data
        form = QuestionForm(request.POST)

        # test form data
        if form.is_valid():
            question_asked = form.cleaned_data['question_asked']
            description = form.cleaned_data['description']
            keyword = form.cleaned_data['keyword']
            user = request.user
            UserScore.user_asked_question(user)

            # saving the form data
            post = Question.objects.create(
                user_obj_id=user.id,
                question_asked=question_asked,
                description=description,
                keyword=keyword,
            )
            url = reverse('stacked:detail_view', kwargs=({'question_id': post.id}))
            print(url)
            return HttpResponseRedirect(url)
    context = {'recent10': Question.get_users_questions(), 'form':form}

    return render(request, 'home/index.html', context)

# Search Functionality
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            question_search = Question.objects.filter(question_asked__icontains=q)
            return render(request, 'movies/search.html',
                          {'results': question_search,
                           'query': q
                           })
    return render(request, 'search/search_form.html', {'error': error})

