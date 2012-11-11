from django.shortcuts import render
from django.http import HttpResponseRedirect

from forms import ConsultaForm

def consulta(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ConsultaForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            form.save()

            return HttpResponseRedirect('home.html') # Redirect after POST
            #return HttpResponse("Dados cadastrados com sucesso!")

    else:
        form = ConsultaForm() # An unbound form

    return render(request, 'cadastro.html', {
        'form': form,
    })