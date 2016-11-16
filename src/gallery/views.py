from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .forms import SearchForm
from .models import Gallery, Comment


class IllustrationCreate(CreateView):
    def get_form_kwargs(self):
        return super().get_form_kwargs()

    template_name = 'add_illust.html'
    model = Gallery
    fields = [
        'name',
        'description',
        'work',
        'status',
    ]

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return redirect('galleries:list')


class IllustrationEdit(UpdateView):
    template_name = 'illust_edit.html'
    model = Gallery
    fields = [
        'name',
        'description',
        'status',
    ]
    success_url = '/'


class IllustrationList(ListView):
    template_name = 'member_illust_list.html'
    context_object_name = 'gallery'
    model = Gallery

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        return super(IllustrationList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Gallery.objects.all()
        if self.search_form.is_valid():
            queryset = queryset.filter(name__icontains=self.search_form.cleaned_data['search'])
            return queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IllustrationList, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


class IllustrationView(CreateView):
    model = Comment
    template_name = 'member_illust.html'
    fields = ('text',)
    success_url = '.'

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.gallery = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.gallery = get_object_or_404(Gallery, id=pk)
        return super(IllustrationView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IllustrationView, self).get_context_data(**kwargs)
        context['gallery'] = self.gallery
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.work = self.gallery
        instance.save()
        return redirect('.')

    def get_success_url(self):
        return '.'
