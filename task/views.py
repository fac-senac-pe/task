from django.shortcuts import render

def lista_tarefas(request):
    tarefas = ["Django", 
               "Projeto", 
               "Python é massa",
               "Estudar",]
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
