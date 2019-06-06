from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, QuestionPaper
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic


def moderator_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return render(request, 'moderator/instructions.html')
        else:
            return render(request, 'moderator/login.html')
    return render(request, 'moderator/login.html')


@login_required(login_url='/moderator/login/')
def index(request):
    if request.method == 'POST':
        checked_list = request.POST.getlist('checks')
        if len(checked_list) != 14:
            url = ''
            resp_body = '<script>alert("Please follow Paper Pattern!!");\
                         window.location="%s"</script>' % url
            return HttpResponse(resp_body)
        count1 = 0
        count2 = 0
        count3 = 0
        for item in checked_list:
            if item.startswith('f'):
                count1 = count1+1
        for item in checked_list:
            if item.startswith('a'):
                count2 = count2+1
        for item in checked_list:
            if item.startswith('g'):
                count3 = count3 + 1
        if count1 != 4 & count2 != 5 & count3 != 5:
            url = ''
            resp_body = '<script>alert("Please follow Paper Pattern!!");\
                         window.location="%s"</script>' % url
            return HttpResponse(resp_body)
        f1 = Question.objects.get(q=checked_list[0])
        f2 = Question.objects.get(q=checked_list[1])
        f3 = Question.objects.get(q=checked_list[2])
        f4 = Question.objects.get(q=checked_list[3])
        a1 = Question.objects.get(q=checked_list[4])
        a2 = Question.objects.get(q=checked_list[5])
        a3 = Question.objects.get(q=checked_list[6])
        a4 = Question.objects.get(q=checked_list[7])
        a5 = Question.objects.get(q=checked_list[8])
        g1 = Question.objects.get(q=checked_list[9])
        g2 = Question.objects.get(q=checked_list[10])
        g3 = Question.objects.get(q=checked_list[11])
        g4 = Question.objects.get(q=checked_list[12])
        g5 = Question.objects.get(q=checked_list[13])
        context = {
            'f1': f3,
            'f2': f4,
            'f3': f1,
            'f4': f2,
            'a1': a4,
            'a2': a5,
            'a3': a1,
            'a4': a2,
            'a5': a3,
            'g1': g4,
            'g2': g5,
            'g3': g1,
            'g4': g2,
            'g5': g3,
        }
        QuestionPaper.objects.create(
            q11=f3.q, q12=f4.q, q13=f1.q, q14=f2.q, q21=a4.q, q22=a5.q, q23=a1.q, q24=a2.q, q25=a3.q, q31=g4.q, q32=g5.q, q33=g1.q, q34=g2.q, q35=g3.q
        )
        return render(request, 'moderator/ppr_prev.html', context)
    f_01 = Question.objects.filter(q__startswith='f_01_')
    f_02 = Question.objects.filter(q__startswith='f_02_')
    f_03 = Question.objects.filter(q__startswith='f_03_')
    f_04 = Question.objects.filter(q__startswith='f_04_')
    a_01 = Question.objects.filter(q__startswith='a_01_')
    a_02 = Question.objects.filter(q__startswith='a_02_')
    a_03 = Question.objects.filter(q__startswith='a_03_')
    g_01 = Question.objects.filter(q__startswith='g_01_')
    g_02 = Question.objects.filter(q__startswith='g_02_')
    g_03 = Question.objects.filter(q__startswith='g_03_')
    context = {
        'f_01': f_01,
        'f_02': f_02,
        'f_03': f_03,
        'f_04': f_04,
        'a_01': a_01,
        'a_02': a_02,
        'a_03': a_03,
        'g_01': g_01,
        'g_02': g_02,
        'g_03': g_03,
    }
    return render(request, 'moderator/index.html', context)


def moderator_logout(request):
    logout(request)
    return render(request, 'moderator/login.html')


@login_required(login_url='/moderator/login/')
def fill_in_the_blanks(request):
    if request.method == 'POST':
        q = request.POST.get('chapter')
        question = request.POST.get('question')
        prev_ppr = request.POST.get('prev_ppr')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        options = option1 + ', ' + option2 + ', ' + option3
        answer = request.POST.get('answer')
        q_no = Question.objects.filter(q__startswith=q).count()
        q_no = q_no + 1
        q_no = str(q_no)
        if len(q_no) == 1:
            q = q + '0' + q_no
        else:
            q = q + q_no
        Question.objects.create(
            q=q, question=question, prev_ppr=prev_ppr, options=options, answer=answer
        )
        return redirect('index')
    return render(request, 'moderator/fill_in_the_blanks.html')


@login_required(login_url='/moderator/login/')
def ans_the_foll(request):
    if request.method == 'POST':
        q = request.POST.get('chapter')
        question = request.POST.get('question')
        prev_ppr = request.POST.get('prev_ppr')
        answer = request.POST.get('answer')
        c_ky = request.POST.get('c_ky')
        v_ky = request.POST.get('v_ky')
        q_no = Question.objects.filter(q__startswith=q).count()
        q_no = q_no + 1
        q_no = str(q_no)
        if len(q_no) == 1:
            q = q + '0' + q_no
        else:
            q = q + q_no
        Question.objects.create(
            q=q, question=question, prev_ppr=prev_ppr, answer=answer, c_ky=c_ky, v_ky=v_ky
        )
        return redirect('index')
    return render(request, 'moderator/ans_the_foll.html')


@login_required(login_url='/moderator/login/')
def give_reasons(request):
    if request.method == 'POST':
        q = request.POST.get('chapter')
        question = request.POST.get('question')
        prev_ppr = request.POST.get('prev_ppr')
        answer = request.POST.get('answer')
        c_ky = request.POST.get('c_ky')
        v_ky = request.POST.get('v_ky')
        q_no = Question.objects.filter(q__startswith=q).count()
        q_no = q_no + 1
        q_no = str(q_no)
        if len(q_no) == 1:
            q = q + '0' + q_no
        else:
            q = q + q_no
        Question.objects.create(
            q=q, question=question, prev_ppr=prev_ppr, answer=answer, c_ky=c_ky, v_ky=v_ky
        )
        return redirect('index')
    return render(request, 'moderator/give_reasons.html')


@login_required(login_url='/moderator/login/')
def sample_ppr(request):
    return render(request, 'moderator/sample_ppr.html')


class FillInTheBlanksDetailView(generic.DetailView):
    model = Question
    template_name = 'moderator/fill_in_the_blanks_detail.html'


class AnswerTheFollDetailView(generic.DetailView):
    model = Question
    template_name = 'moderator/ans_the_foll_detail.html'


class GiveReasonDetailView(generic.DetailView):
    model = Question
    template_name = 'moderator/give_reason_detail.html'
