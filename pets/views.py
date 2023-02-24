from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Pets
from .forms import PetForm


def index(request) -> HttpResponse:
    """
    Default view for pets app

    Displays list of Pets in database

    Args:
        request(dict): request object

    Raises:
        Http404(str): No pets exist in storage!

    Returns:
        HttpResponse (obj): Response object
    """
    try:
        pets = Pets.objects.order_by("pk")
    except Pets.DoesNotExist:
        raise Http404("No pets exist in storage!")
    return render(request, "index.html", {"pets": pets})


def create(request) -> HttpResponse:
    """
    create New Pet

    Arguments:
        request(obj): Http request object

    Returns:
        HttpResponse(obj): Http response object
    """
    context = {}
    form: PetForm = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "form.html", context)


def edit(request, id) -> HttpResponse:
    """
    update pet object

    Args:
        request (dict): http request object
        id (int): id

    Returns:
        HttpResponse: object - HTTP Response object
    """
    context = {}
    pet: Pets = get_object_or_404(Pets, id=id)
    context["pet"] = pet
    form: PetForm = PetForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form
    return render(request, "form.html", context)
