from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
            Column('title', css_class='col-md-6 col-sm-12 mb-0'),
            Column('due_date', css_class='col-md-2 col-sm-12 mb-0'),
            Column('category', css_class='col-md-2 col-sm-12 mb-0'),
            Column(Submit('submit', 'Add Task'), css_class='col-md-2 col-sm-12 align-self-end mb-3'),
            css_class='form-row'
            )
        )