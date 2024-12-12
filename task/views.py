from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tarefa
from .forms import TarefaForm

@login_required
def lista_tarefas(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST, request.FILES)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('lista_tarefas')
        else:
            messages.error(request, 'Erro ao adicionar a tarefa. Verifique os dados informados.')
    else:
        form = TarefaForm()

    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas, 'form': form})

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, request.FILES, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('lista_tarefas')
        else:
            messages.error(request, 'Erro ao atualizar a tarefa. Verifique os dados informados.')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'editar_tarefa.html', {'form': form})