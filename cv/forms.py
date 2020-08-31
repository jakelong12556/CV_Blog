from django import forms

from .models import Experiences


class CV_Form(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ('work_title', 'start_end_dates',
                  'company', 'experience_desp')
