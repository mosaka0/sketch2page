from django.shortcuts import render, redirect

from .forms import ImageForm
from converterApi.converter_main import converter_run


def upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save()

            converter_run(form_obj.image.name)

            return redirect('result')

    else:
        form = ImageForm()

    return render(request, 'upload-template.html', {'form': form})


def result_view(request):
    return render(request, 'result.html')
