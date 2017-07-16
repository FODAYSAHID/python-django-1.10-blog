from django import forms

class ContactForm(forms.Form):

	full_name = forms.CharField(label = "Full Name", max_length = 70, required = True)

	email = forms.EmailField(label = "Email Address", required = True)

	subject = forms.CharField(label = "Subject", required = True)

	message = forms.CharField(label = "Message", required = True, widget = forms.Textarea(attrs = {"class":"materialize-textarea"}))