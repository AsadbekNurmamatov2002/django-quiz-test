from django.shortcuts import render, get_object_or_404
from .models import Fanmavzusi
from django.http import JsonResponse
from questions.models import Savol, Varyant
from results.models import Results
from users.models import Profile, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


@login_required(login_url="users:login")
def quiz_list(request):
    id=request.user.id
    user = get_user_model().objects.get(id=id)
    if user.age<=12:
        quizs=Fanmavzusi.objects.all().Boshlangich()
    elif user.age<=16 and user.age>12:
        quizs=Fanmavzusi.objects.all().Ortacha()
    else:
        quizs=Fanmavzusi.objects.all().Kattalar()
    print(quizs)
    print(request.user)
    if user:
        user_profil=get_object_or_404(Profile, user=user)
        results=user.results_set.all().order_by('-id')
    
    return render(request, "page/quiz.html", {"quizs":quizs, 'user':user, 'user_profil':user_profil, "results":results})


@login_required(login_url="users:login")
def quiz_datiel(request, pk):
    quiz=get_object_or_404(Fanmavzusi, id=pk)
    return render(request, 'page/quizdatiel.html', {"quiz":quiz})


@login_required(login_url="users:login")
def quiz_data_json(request, pk):
    quiz=Fanmavzusi.objects.get(pk=pk)
    questions=[]
    for q in quiz.get_savol():
        answers=[]
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse(
        {'data':questions,
        'vaqti': quiz.vaqti}
    )



@login_required(login_url="users:login")
def save_quiz_data(request, pk):
    print(request.POST)
    questions=[]
    data=request.POST
    data_=dict(data.lists())
    print(data_)
    data_.pop('csrfmiddlewaretoken')
    print(data_)
    for k in data_.keys():
        savol=Savol.objects.get(text=k)
        questions.append(savol)
    
    print(questions)
    user=request.user
    quiz=Fanmavzusi.objects.get(pk=pk)
    score=0
    multip=100/quiz.test_soni
    resultes=[]
    nateja=None
    
    for q in questions:
        javob=request.POST.get(q.text)
        print('javob',javob)
        if javob !="":
            q_answer=Varyant.objects.filter(savol=q)
            for a in q_answer:
                if javob==a.text:
                    if a.tugri_yoke_natugri:
                        score+=1
                        nateja=a.text
                else:
                    if a.tugri_yoke_natugri:
                        nateja=a.text
            resultes.append({str(q):{"nateja":nateja, "nateja_a":javob}})
        else:
            resultes.append({str(q): "javob berilmagan"})
    score_=score*multip
    Results.objects.create(quiz=quiz, user=user, score=score_)
    if score_>=quiz.utish_foizi:
        return JsonResponse({'passed,': True, "score":score_, "results": resultes})
    else:
        return JsonResponse({'passed,': False, "score":score_, "results":resultes})