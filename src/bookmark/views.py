from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView

from gallery.models import Gallery
from .models import Bookmark


class BookmarkView(CreateView):
    model = Bookmark
    template_name = 'bookmark.html'
    fields = ('comment',)
    success_url = 'galleries:list'

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.gallery = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.gallery = get_object_or_404(Gallery, id=pk)
        return super(BookmarkView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookmarkView, self).get_context_data(**kwargs)
        context['gallery'] = self.gallery
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.work = self.gallery
        instance.save()
        return redirect('galleries:list')
