from django.shortcuts import render
from .models import Artist, Studio, Engineer, Session
from .forms import SessionForm
from django.forms import formset_factory

def home(request):
    artist = Artist.objects
    return render(request, 'scheduler/home.html', {"home": home})


def artists(request):
    artists = Artist.objects.all()

    return render(request, 'scheduler/artists.html', {"artists": artists})

def studios(request):
    studios = Studio.objects.all()

    return render(request, 'scheduler/studios.html', {"studios": studios})

def engineers(request):
    engineers = Engineer.objects.all()

    return render(request, 'scheduler/engineers.html', {"engineers": engineers})

def sessions(request):
    sessions = Session.objects.all()

    return render(request, 'scheduler/sessions.html', {"sessions": sessions})

def createsession(request):
    #multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = SessionForm(request.POST, request.FILES)
        if filled_form.is_valid():
            created_session = filled_form.save()
            created_session_pk = created_session.id
            note = 'You\'ve just create a session for %s at %s with %s on %s' % (
                filled_form.cleaned_data['artist'],
                filled_form.cleaned_data['studio'],
                filled_form.cleaned_data['engineer'],
                filled_form.cleaned_data['appointment_date'])
            filled_form = SessionForm()
        else:
            created_pizza_pk = None
            note = 'Your session was not created, please try again.'

        return render(request, 'scheduler/create_session.html', {'created_session_pk': created_session_pk, 'sessionform': filled_form, 'note': note})
    else:
        form = SessionForm()
        return render(request, 'scheduler/create_session.html', {'sessionform': form})
