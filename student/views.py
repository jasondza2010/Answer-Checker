from django.shortcuts import render
from .models import StudentAnswer, Result
from moderator.models import QuestionPaper, Question
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import language_check
import Levenshtein
from multiprocessing import Process
import sys
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from PyDictionary import PyDictionary
from nltk.corpus import wordnet


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return render(request, 'student/instructions.html')
        else:
            return render(request, 'student/login.html')
    return render(request, 'student/login.html')


@login_required(login_url='/student/login/')
def indexx(request):
    questions = QuestionPaper.objects.all().last()
    q11 = questions.q11
    q11 = Question.objects.filter(q=q11)
    q11_op = q11[0].options
    q11 = q11[0].question
    q12 = questions.q12
    q12 = Question.objects.filter(q=q12)
    q12_op = q12[0].options
    q12 = q12[0].question
    q13 = questions.q13
    q13 = Question.objects.filter(q=q13)
    q13_op = q13[0].options
    q13 = q13[0].question
    q14 = questions.q14
    q14 = Question.objects.filter(q=q14)
    q14_op = q14[0].options
    q14 = q14[0].question
    q21 = questions.q21
    q21 = Question.objects.filter(q=q21)
    q21 = q21[0].question
    q22 = questions.q22
    q22 = Question.objects.filter(q=q22)
    q22 = q22[0].question
    q23 = questions.q23
    q23 = Question.objects.filter(q=q23)
    q23 = q23[0].question
    q24 = questions.q24
    q24 = Question.objects.filter(q=q24)
    q24 = q24[0].question
    q25 = questions.q25
    q25 = Question.objects.filter(q=q25)
    q25 = q25[0].question
    q31 = questions.q31
    q31 = Question.objects.filter(q=q31)
    q31 = q31[0].question
    q32 = questions.q32
    q32 = Question.objects.filter(q=q32)
    q32 = q32[0].question
    q33 = questions.q33
    q33 = Question.objects.filter(q=q33)
    q33 = q33[0].question
    q34 = questions.q34
    q34 = Question.objects.filter(q=q34)
    q34 = q34[0].question
    q35 = questions.q35
    q35 = Question.objects.filter(q=q35)
    q35 = q35[0].question
    context = {
        'q11': q11,
        'q11_op': q11_op,
        'q12': q12,
        'q12_op': q12_op,
        'q13': q13,
        'q13_op': q13_op,
        'q14': q14,
        'q14_op': q14_op,
        'q21': q21,
        'q22': q22,
        'q23': q23,
        'q24': q24,
        'q25': q25,
        'q31': q31,
        'q32': q32,
        'q33': q33,
        'q34': q34,
        'q35': q35,
    }
    return render(request, 'student/student_answer_form.html', context)


def result(request):
    username = request.user
    if request.method == 'POST':
        q21_c_ky=[]
        q21_v_ky=[]
        q22_c_ky = []
        q22_v_ky = []
        q23_c_ky = []
        q23_v_ky = []
        q24_c_ky = []
        q24_v_ky = []
        q25_c_ky = []
        q25_v_ky = []
        q31_c_ky = []
        q31_v_ky = []
        q32_c_ky=[]
        q32_v_ky=[]
        q33_c_ky = []
        q33_v_ky = []
        q34_c_ky = []
        q34_v_ky = []
        q35_c_ky = []
        q35_v_ky = []
        ansq11 = request.POST.get('q11')
        ansq12 = request.POST.get('q12')
        ansq13 = request.POST.get('q13')
        ansq14 = request.POST.get('q14')
        ansq21 = request.POST.get('q21')
        ansq22 = request.POST.get('q22')
        ansq23 = request.POST.get('q23')
        ansq24 = request.POST.get('q24')
        ansq25 = request.POST.get('q25')
        ansq31 = request.POST.get('q31')
        ansq32 = request.POST.get('q32')
        ansq33 = request.POST.get('q33')
        ansq34 = request.POST.get('q34')
        ansq35 = request.POST.get('q35')
        questions = QuestionPaper.objects.all().last()
        q11 = questions.q11
        q11 = Question.objects.filter(q=q11)
        q11_ans = q11[0].answer
        q11 = evaluate_fill_ups(q11_ans, ansq11)
        q12 = questions.q12
        q12 = Question.objects.filter(q=q12)
        q12_ans = q12[0].answer
        q12 = evaluate_fill_ups(q12_ans, ansq12)
        q13 = questions.q13
        q13 = Question.objects.filter(q=q13)
        q13_ans = q13[0].answer
        q13 = evaluate_fill_ups(q13_ans, ansq13)
        q14 = questions.q14
        q14 = Question.objects.filter(q=q14)
        q14_ans = q14[0].answer
        q14 = evaluate_fill_ups(q14_ans, ansq14)
        q1_tot = q11+q12+q13+q14
        q1_tot = round(q1_tot)
        q21 = questions.q21
        q21 = Question.objects.filter(q=q21)
        q21_c_ky = q21[0].c_ky
        q21_c_ky = q21_c_ky.split(';')
        q21_v_ky = q21[0].v_ky
        q21_v_ky = q21_v_ky.split(';')
        q21 = evaluate_answer(ansq21, q21_c_ky, q21_v_ky)
        q22 = questions.q22
        q22 = Question.objects.filter(q=q22)
        q22_c_ky = q22[0].c_ky
        q22_c_ky = q22_c_ky.split(';')
        q22_v_ky = q22[0].v_ky
        q22_v_ky = q22_v_ky.split(';')
        q22 = evaluate_answer(ansq22, q22_c_ky, q22_v_ky)
        q23 = questions.q23
        q23 = Question.objects.filter(q=q23)
        q23_c_ky = q23[0].c_ky
        q23_c_ky = q23_c_ky.split(';')
        q23_v_ky = q23[0].v_ky
        q23_v_ky = q23_v_ky.split(';')
        q23 = evaluate_answer(ansq23, q23_c_ky, q23_v_ky)
        q24 = questions.q24
        q24 = Question.objects.filter(q=q24)
        q24_c_ky = q24[0].c_ky
        q24_c_ky = q24_c_ky.split(';')
        q24_v_ky = q24[0].v_ky
        q24_v_ky = q24_v_ky.split(';')
        q24 = evaluate_answer(ansq24, q24_c_ky, q24_v_ky)
        q25 = questions.q25
        q25 = Question.objects.filter(q=q25)
        q25_c_ky = q25[0].c_ky
        q25_c_ky = q25_c_ky.split(';')
        q25_v_ky = q25[0].v_ky
        q25_v_ky = q25_v_ky.split(';')
        q25 = evaluate_answer(ansq25, q25_c_ky, q25_v_ky)
        q2_tot = q21+q22+q23+q24+q25
        m = min(q21, q22, q23, q24, q25)
        q2_tot = q2_tot-m
        q2_tot = round(q2_tot)
        q31 = questions.q31
        q31 = Question.objects.filter(q=q31)
        q31_c_ky = q31[0].c_ky
        q31_c_ky = q31_c_ky.split(';')
        q31_v_ky = q31[0].v_ky
        q31_v_ky = q31_v_ky.split(';')
        q31 = evaluate_answer(ansq31, q31_c_ky, q31_v_ky)
        q32 = questions.q32
        q32 = Question.objects.filter(q=q32)
        q32_c_ky = q32[0].c_ky
        q32_c_ky = q32_c_ky.split(';')
        q32_v_ky = q32[0].v_ky
        q32_v_ky = q32_v_ky.split(';')
        q32 = evaluate_answer(ansq32, q32_c_ky, q32_v_ky)
        q33 = questions.q33
        q33 = Question.objects.filter(q=q33)
        q33_c_ky = q33[0].c_ky
        q33_c_ky = q33_c_ky.split(';')
        q33_v_ky = q33[0].v_ky
        q33_v_ky = q33_v_ky.split(';')
        q33 = evaluate_answer(ansq33, q33_c_ky, q33_v_ky)
        q34 = questions.q34
        q34 = Question.objects.filter(q=q34)
        q34_c_ky = q34[0].c_ky
        q34_c_ky = q34_c_ky.split(';')
        q34_v_ky = q34[0].v_ky
        q34_v_ky = q34_v_ky.split(';')
        q34 = evaluate_answer(ansq34, q34_c_ky, q34_v_ky)
        q35 = questions.q35
        q35 = Question.objects.filter(q=q35)
        q35_c_ky = q35[0].c_ky
        q35_c_ky = q35_c_ky.split(';')
        q35_v_ky = q35[0].v_ky
        q35_v_ky = q35_v_ky.split(';')
        #len_v_ky = len(q35_v_ky)
        #for i in range(0, len_v_ky):
            #q35_v_ky[i] = q35_v_ky[i].split(',')
        q35 = evaluate_answer(ansq35, q35_c_ky, q35_v_ky)
        q3_tot = q31+q32+q33+q34+q35
        m = min(q31, q32, q33, q34, q35)
        q3_tot = q3_tot-m
        q3_tot = round(q3_tot)
        tot = q1_tot+q2_tot+q3_tot
        tot = round(tot)
        context = {
            'username': username,
            'q11': q11,
            'q12': q12,
            'q13': q13,
            'q14': q14,
            'q1_tot': q1_tot,
            'q21': q21,
            'q22': q22,
            'q23': q23,
            'q24': q24,
            'q25': q25,
            'q2_tot': q2_tot,
            'q31': q31,
            'q32': q32,
            'q33': q33,
            'q34': q34,
            'q35': q35,
            'q3_tot': q3_tot,
            'tot': tot,
        }

        StudentAnswer.objects.create(
            seat_no=str(username),
            q11=ansq11,
            q12=ansq12,
            q13=ansq13,
            q14=ansq14,
            q21=ansq21,
            q22=ansq22,
            q23=ansq23,
            q24=ansq24,
            q25=ansq25,
            q31=ansq31,
            q32=ansq32,
            q33=ansq33,
            q34=ansq34,
            q35=ansq35
        )
        Result.objects.create(
            seat_no=str(username),
            q11=str(q11),
            q12=str(q12),
            q13=str(q13),
            q14=str(q14),
            q1_tot=str(q1_tot),
            q21=str(q21),
            q22=str(q22),
            q23=str(q23),
            q24=str(q24),
            q25=str(q25),
            q2_tot=str(q2_tot),
            q31=str(q31),
            q32=str(q32),
            q33=str(q33),
            q34=str(q34),
            q35=str(q35),
            q3_tot=str(q3_tot),
            tot=str(tot),
        )
        student_logout(request)
    return render(request, "student/result.html", context)


def student_logout(request):
    logout(request)
    return 0


def evaluate_fill_ups(model_ans, student_ans):
    if model_ans == student_ans:
        return 1.0
    else:
        return 0.0


def evaluate_answer(text, c_ky, v_ky):
    if text == "":
        return 0.0
    tool = language_check.LanguageTool('en-IN')
    ps = PorterStemmer()
    total_marks = 2
    marksc = 0
    marksv = 0
    marks = 0
    temp1 = len(c_ky)
    if not v_ky:
        temp2 = 0
    else:
        temp2 = len(v_ky)
    temp3 = temp1 + temp2
    marks_per_ky = total_marks / temp3

    antonyms = []
    a = 0
    sp = text.split()
    var = []
    target = "not"

    for i, w in enumerate(sp):
        if w == target:
            var.append(sp[i + 1])

    for i in range(0, len(v_ky)):
        v_ky[i] = v_ky[i].split()

#Variable keywords
    for i in range(0, len(v_ky)):
        if not v_ky[0]:
            break
        for syn in wordnet.synsets(v_ky[i][0]):
            for l in syn.lemmas():
                v_ky[i].append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())

    for i in range(0, len(v_ky)):
        if not v_ky[0]:
            break
        for j in range(0, len(v_ky[i])):
            v_ky[i][j] = ps.stem(v_ky[i][j])
            v_ky[i][j] = v_ky[i][j].replace("_", " ")

    for i in range(0, len(v_ky)):
        if not v_ky[0]:
            break
        for j in range(0, len(v_ky[i])):
            if v_ky[i][j] in text:
                marksv = marksv + marks_per_ky
                break
            #elif not antonyms:
                #break
            #elif antonyms[j] in var:
                #marksv = marksv + marks_per_ky
                #break
#Constant keywords
    for i in range(0, len(c_ky)):
        for j in range(0, (len(text) - len(c_ky))):
            if (Levenshtein.distance(c_ky[i], text[j:(len(c_ky[i]) + j)])) <= len(c_ky[i]) / 7:
                marksc = marksc + marks_per_ky
                break
    marks = marksc + marksv
    if marks == 0:
        return 0.0
    #Negation condition
    for i in range(0, len(v_ky)):
        if not v_ky[0]:
            break
        for j in range(0, len(v_ky[i])):
            if v_ky[i][j] in var:
                marks = marks - 0.5

#Grammar Correction
    matches = tool.check(text)
    no = len(matches)
    if no != 0:
        marks = marks - 0.5
    final_score = str(marks)
    return round(float(final_score) * 2) / 2
