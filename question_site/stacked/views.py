from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Question, Answer
from .forms.question_form import QuestionForm, AnswerForm
from accounts.models import UserScore

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Require login
from django.contrib.auth.decorators import login_required


class QuestionList(ListView):
    model = Question



@login_required(login_url='/accounts/login/')
def question_input_form(request):
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

    return render(
        request,
        'forms/question_form.html',
        {
            'form': form,
        }
    )


@login_required(login_url='/accounts/login/')
def detail(request, question_id):
    responses = Answer.objects.filter(question_obj_id=question_id).order_by('-score')

    if request.method == 'GET':
        form = AnswerForm()

    elif request.method =='POST' and 'answer' in request.POST:
        # take in the form data
        form = AnswerForm(request.POST)
        # test form data
        if form.is_valid():
            user = request.user
            response = form.cleaned_data['response']
            # saving the form data
            post = Answer.objects.create(
                user_obj_id=user.id,
                question_obj_id=question_id,
                response=response,
                score=0,
            )
            return HttpResponseRedirect('/questions/{}'.format(question_id))

    elif request.method =='POST' and 'upvote' in request.POST:
        answer_id = request.POST.get('answer_id')

        upvoted_answer = Answer.objects.get(id=answer_id)
        upvoted_answer.score += 10

        answer_author = upvoted_answer.user_obj_id
        UserScore.user_asked_question(answer_author)

        upvoted_answer.save()

        return HttpResponseRedirect('/questions/{}'.format(question_id))

    elif request.method == 'POST' and 'downvote' in request.POST:
        answer_id = request.POST.get('answer_id')

        downvoted_answer = Answer.objects.get(id=answer_id)
        downvoted_answer.score -= 10

        answer_author = downvoted_answer.user_obj_id
        UserScore.user_asked_question(answer_author)

        downvoted_answer.save()

        return HttpResponseRedirect('/questions/{}'.format(question_id))

    question = get_object_or_404(Question, id=question_id)
    context = {'question': question, 'form': form, 'responses': responses}
    return render(request, 'stacked/detail.html', context)
