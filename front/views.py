from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import Machine
from django.core.paginator import Paginator
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required


def acc_login(request):
    error_msg=' '
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            print(user)
            print(type(user))
            login(request, user)
            return redirect(request.GET.get("next", '/index'))
        else:
            print(user)
            print(type(user))
            error_msg = "用户名或密码错误"
        return render(request, "login.html", {"error_msg": error_msg})

def acc_logout(request):
    logout(request)
    return redirect('/login')

@login_required
def index(request):
    # render_to_response('index.html')
    return render(request, 'index.html')

def mac(request):
    # mac_list = Machine.objects.all()
    # paginator = Paginator(mac_list, 10)
    # page = request.GET.get('page')
    # macs = paginator.get_page(page)
    # page = macs
    # return render(request, 'mac.html', locals())
    mac_list = Machine.objects.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data.get("keyword")
            if keyword:
                mac_list = Machine.objects.filter(mac_id__icontains=keyword)
                # return render(request, 'search.html', locals())
    else:
        form = SearchForm()
    paginator = Paginator(mac_list, 10)
    page = request.GET.get('page')
    macs = paginator.get_page(page)
    page = macs
    return render(request, 'mac.html', locals())
    # return render(request, 'mac.html', {'form': form, 'macs': mac_list})

# class MacView(ListView):
#     model = Machine
#     paginate_by = 10

def mac_search(request):
    macs = Machine.objects.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data.get("keyword")
            if keyword:
                mac_list = Machine.objects.filter(mac_id__icontains=keyword)
                return HttpResponseRedirect(request, 'search.html', {'form': form, 'mac_list': mac_list})
                # return render(request, 'search.html', locals())
    else:
        form = SearchForm()
    return render(request, 'mac.html', locals())
    # return render(request, 'search.html', {'form': form, 'mac_list': False, })

def ajax_search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        model = request.GET.get('model')
        field1 = request.GET.get('field1')
        field2 = request.GET.get('field2')
        print(model + ':' + field1 + field2)
        if keyword:
            # res = Machine.objects.filter(mac_id__icontains=keyword)
            # res = Machine.objects.filter(Q(mac_id__icontains=keyword) | Q(ipmi__icontains=keyword))
            # res = eval(model + '.objects.filter(' + field + '__icontains=keyword)')
            res = eval(model + '.objects.filter(Q(' + field1 + '__icontains=keyword) | Q(' + field2 + '__icontains=keyword))')
            data = serializers.serialize('json', res)
            print(data)
            return JsonResponse(data, safe=False)





def ops(request):
    ops_list = Machine.objects.all()
    paginator = Paginator(ops_list, 20)
    page = request.GET.get('page')
    ops = paginator.get_page(page)
    page = ops
    return render(request, 'mac.html', locals())

def addmainten(request):
    if request.method == 'POST':
        form = MaintenanceFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('sucess')
    else:
        form = MaintenanceFrom()
    return render(request, 'addMaintenance.html', {'form': form})


# def addmac(request):
#     if request.method == 'POST':
#         form = macform(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('sucess')
#     else:
#         form = macform()
#     return render(request, 'addmac.html', {'form': form})

# def addmac(request):
#     if request.method == 'POST':
#         form = MacForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('sucess')
#     else:
#         form = macformset()
#     return render(request, 'addmac.html', {'formset': form})





