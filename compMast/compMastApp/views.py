from django.shortcuts import render, redirect
from .forms import UserInputForm

def input_form(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.save()
            # Add your processing algorithm here
            processed_text = user_input.text.upper()  # Example: Uppercase the text
            return render(request, 'result.html', {'processed_text': processed_text})
    else:
        form = UserInputForm()
    return render(request, 'input_form.html', {'form': form})
