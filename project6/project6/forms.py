from django import forms


class userForm(forms.Form):
    num1 = forms.CharField(label="Value1 ")
    num2 = forms.CharField(label="Value2 ")
    # email = forms.EmailField(label="Email ", required=False)
