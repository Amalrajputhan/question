from django import forms

from .models import Department, Courses

class LocationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    dob = forms.DateField(label='DOB')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(
        label='Gender',
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        widget=forms.RadioSelect()
    )
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', max_length=450)
    purpose = forms.ChoiceField(label='Purpose', choices=[('enquiry', 'Enquiry'), ('placeorder', 'Placeorder')])
    # Updated dynamically in the view
    materials_provide = forms.MultipleChoiceField(
        label='Materials Provide',
        choices=[
            ('debit_note_book', 'Debit Note Book'),
            ('pen', 'Pen'),
            ('exam_papers', 'Exam Papers'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    department = forms.ModelChoiceField(queryset=Department.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_courses/", "hx-target": "#id_courses"}))
    courses = forms.ModelChoiceField(queryset=Courses.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "department" in self.data:
            department_id = int(self.data.get("department"))
            self.fields["courses"].queryset = Courses.objects.filter(department_id=department_id)