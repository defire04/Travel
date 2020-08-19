from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render
from cities.models import City
from cities.forms import HtmlForm, CityForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator

def home(request, pk=None):
#    if request.method == 'POST':
#        print(request.POST)
#        print('-' * 10)
#        print(request.POST.get('name'))
#    if pk:
#        city = City.objects.filter(pk=pk).first()
#       return render(request, 'cities/detail.html', {'object':city})
#    cities = City.objects.all()
#   context = {'objects_list':cities,}
#    return render(request, 'cities/home.html', context)
#    if request.method == 'POST':
#        form = CityForm(request.POST or None)
#        if form.is_valid():
#            print(form.cleaned_data)
#           form.save()
#
#            name = form.cleaned_data.get('name')
#            city = City(name=name)                 - для доп поллей 
#            city.save() 
#    form = CityForm()
#    cities = City.objects.all()
#    context = {'objects_list': cities, 'form': form}
#    return render(request, 'cities/home.html', context)
    cities = City.objects.all()
    paginator = Paginator(cities, 4)
    page = request.GET.get('page')
    cities = paginator.get_page(page)
    context = {'objects_list':cities,}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object' # По умолчанию для DetailView
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно создан!'


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

#    def get(self, request, *args, **kwargs):
#        """Для избежания подтверждающего действия в удалить """
#       return self.post(request, *args, **kwargs)
