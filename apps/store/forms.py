from django import forms


CHOICES_LIST = (('ascending_date', 'возрастанию даты'), ("descending_date", 'убыванию даты'), )


class SortedByDateForm(forms.Form):
    sorted_by = forms.ChoiceField(choices=CHOICES_LIST, label='Сортировать по', required=False)
