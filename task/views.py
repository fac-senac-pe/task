from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})

def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')