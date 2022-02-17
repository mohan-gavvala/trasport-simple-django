from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from Q_and_A_app.models import Question, Answer
from Q_and_A_app.forms import RegisterUserForm, LoginForm,Add_Question_Form,Add_Response_Form
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User

def registerPage(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        try:
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
                #return HttpResponse('ok')
        except Exception as e:
            print(e)
            raise

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def loginPage(request):
    form = LoginForm()

    if request.method == 'POST':
        try:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'login.html', context)

@login_required(login_url='register')
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def newQuestionPage(request):
    form = Add_Question_Form()

    if request.method == 'POST':
        try:
            form = Add_Question_Form(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
                return redirect('home')

        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'new-question.html', context)

def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    # for x in questions:
    #         print(x.ask_question)
    context = {
        'questions': questions
    }
    return render(request, 'homepage.html', context)

def questionPage(request, id):
    response_form = Add_Response_Form()
    if request.method == 'POST':

        # print('ok1')
        try:
            response_form = Add_Response_Form(request.POST)
            # print('ok2')
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                print('ok3')
                # return HttpResponse ('ok')
                s='/question/'+str(id)+'#'+str(response.id)
                # print(s)
                return redirect(s)
        except Exception as e:
            print(e)
            raise
#
    question = Question.objects.get(id=id)


    context = {
        'question': question,

        'response_form': response_form,



    }
    return render(request, 'question.html', context)
@login_required(login_url='login')    
def LikeView(request,pk):
    print("ID:",id)
    post=get_object_or_404(Answer,id=request.POST.get('response_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('/')
