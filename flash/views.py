from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Card
from .forms import NewProfileForm,NewCardForm





# Create your views here.

@login_required(login_url='/accounts/login')
def welcome(request):
    cards = Card.objects.all()
    return render(request,'index.html',{"cards":cards})


def search_results(request):

    if 'subject' in request.GET and request.GET["subject"]:
        search_term = request.GET.get("subject")
        searched_subjects = Subject.search_by_title(search_term)
        message = f"{search_term}"

        return redirect(request, 'search.html',{"message":message,"subjects": searched_projects})

    else:
        message = "Searched"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login')
def profile(request,profile_id):
    profile = Profile.objects.get(pk = profile_id)
    projects = Project.objects.all()
    return render(request,'profile.html',{"profile":profile,"projects":projects})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')
    else:
        form = NewProfileForm()
    return render(request,'new_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def new_card(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewCardForm(request.POST,request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('welcome')

    else:
        form = NewCardForm()
    return render(request, 'new_card.html', {"form": form})



