from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

def HomePageView(request):
    mytodo = Todo.objects.order_by('id')
    form = TodoForm()
    context = { 'mytodo': mytodo, 'form' : form}

    return render(request,'index.html', context)

@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete =True   
    mytodo.save()
    return redirect('index')

def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')





# class HomePageView(TemplateView):
#     template_name = 'index.html'
