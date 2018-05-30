from django.shortcuts import render, HttpResponseRedirect
from art.models import Art


def Detail_handler(request):
    id = request.GET.get("id", None)
    if id:
        art = Art.objects.get(id=int(id))
        context = {"art": art}
        return render(request, "home/detail.html", context=context)
    else:
        return HttpResponseRedirect("/art/index")
