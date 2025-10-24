from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        resp = super().form_valid(form)
        messages.success(self.request, "Account created! Please log in.")
        return resp


def home(request):
    return HttpResponse("<h1>Hello, Django To-Do App!</h1>")



@login_required
def task_list(request):
    status = request.GET.get('status')
    qs = Task.objects.filter(owner=request.user)
    if status == 'open': qs = qs.filter(is_completed=False)
    if status == 'done': qs = qs.filter(is_completed=True)
    return render(request, 'tasks/task_list.html', {'tasks': qs})

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        if title:
            Task.objects.create(owner=request.user, title=title)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

@login_required
def task_toggle(request, pk):
    t = get_object_or_404(Task, pk=pk, owner=request.user)
    t.is_completed = not t.is_completed
    t.save()
    return redirect('task_list')

@login_required
def task_delete(request, pk):
    t = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        t.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': t})

