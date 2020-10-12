from django.shortcuts import render, redirect
from restful_shows_app.models import *
from datetime import datetime
from django.contrib import messages


def all_shows(request):
    show_list = shows.objects.all()
    context = {
        "all_shows" : show_list
    }
    return render(request,'show_list.html',context)

def show_details(request,show_id):
    show_id = shows.objects.get(id=show_id)
    context = {
        "all_show_details" : show_id
    }
    return render(request,'show_details.html',context)

def new_show(request):
    return render(request,'create_new.html')

def edit_page(request,edit_id):
    show_id = shows.objects.get(id=edit_id)
    print(show_id.release_date)
    context = {
        "all_show_details" : show_id,
    }
    return render(request,'edit_show.html',context)

def add_new(request):
    errors = shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST['title'] 
        network = request.POST['network']
        release =request.POST['release_date']
        desc = request.POST['desc']
        shows.objects.create(title=title,network=network,release_date=release,description = desc) 
        return redirect('/shows/'+str(shows.objects.last().id))

def update_show(request,show_id_to_update):
    errors = shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(show_id_to_update)+'/edit')
    else:
        update_show_id = shows.objects.get(id=show_id_to_update)
        update_show_id.title = request.POST['title']
        update_show_id.network = request.POST['network']
        update_show_id.release_date = request.POST['release_date']
        update_show_id.description = request.POST['desc']
        update_show_id.save()
        return redirect('/shows/'+str(show_id_to_update))

def destroy(request,delete_show_id):
    to_delete_id = shows.objects.get(id=delete_show_id)
    to_delete_id.delete()
    return redirect('/shows')