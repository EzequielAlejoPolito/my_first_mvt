from django.shortcuts import render

from my_app.models import Dato

def datos(request):
    datos = Dato.objects.all()

    context_dict = {"datos": datos}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/datos_familia.html",
    )