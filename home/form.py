from cProfile import label
from dataclasses import fields
from datetime import date
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date':  DateInput(),
        
        }
        labels={
            'P_name': "Patient Name",
            'p_phone':"Patient phone",
            'P_email': "Email",
            'doc_name':"Doctor Name",
            'booking_date':"Booking Date",
        }
