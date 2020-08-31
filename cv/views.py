from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
from .models import Experiences
from .forms import CV_Form

# Create your views here.


def cv_base(request):
    cv_list = Experiences.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'CV/cv_base.html', {'cv_list': cv_list})


def cv_edit(request, pk):
    if request.user.is_anonymous:
        return redirect('cv_page')
    cv = get_object_or_404(Experiences, pk=pk)

    if request.method == 'POST':
        form = CV_Form(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save()
            return redirect('cv_page')
    if not cv:
        raise Http404
    form = CV_Form(instance=cv)
    return render(request, 'CV/cv_edit.html', {'form': form})
