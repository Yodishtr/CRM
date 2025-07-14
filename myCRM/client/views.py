from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import AddClientForm
from django.contrib import messages
from team.models import Team


@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'client/clients_list.html', {
        'clients': clients
    })

@login_required
def clients_detail(request, pk):
    clients = Client.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, 'client/clients_detail.html', {
        'client': clients
    })

@login_required
def clients_add(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            client = form.save(commit=False)
            client.created_by = request.user
            client.team = team
            client.save()
            messages.success(request, 'Client has been added successfully')
            return redirect('clients_list')
    else:
        form = AddClientForm()
    return render(request, 'client/clients_add.html', {
        'form': form,
        'team': team
    })

@login_required
def clients_delete(request, pk):
    client = Client.objects.filter(created_by=request.user).get(pk=pk)
    client.delete()
    messages.success(request, 'client was successfully deleted')
    return redirect('clients_list')

@login_required
def clients_edit(request, pk):
    client = Client.objects.filter(created_by=request.user).get(pk=pk)
    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Edit has been successful')
            return redirect('clients_list')
    else:
        form = AddClientForm(instance=client)
    return render(request, 'client/clients_edit.html', {
        'form': form
    })
