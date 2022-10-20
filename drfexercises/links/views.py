from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import generics, viewsets
FAVOURITE_LINKS = [
    'www.google.com', 'www.onet.pl', 'www.flashscore.com', 'www.facebook.com', 'www.allegro.pl'
]


def favourite_links_view(request):
    template = 'links/favourite.html'
    data = {
        'links': FAVOURITE_LINKS,
    }
    return render(request, template, data)


class FavouriteLinksView(TemplateView):
    template_name = "links/favourite.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = FAVOURITE_LINKS
        return context



