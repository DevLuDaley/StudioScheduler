from django import forms
from .models import Artist, Studio, Engineer, Session




class SessionForm(forms.ModelForm):
    class Meta:

        model = Session
        fields = ['appointment_date', 'duration','artist', 'engineer', 'studio', 'status']
        labels = {
            "appointment_date": "Appointment date",
            "duration": "Duration",
            "artist": "Artist",
            "engineer": "Engineer",
            "studio": "Studio",
            "status": "Status",
        }
