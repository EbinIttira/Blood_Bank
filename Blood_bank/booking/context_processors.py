from . models import District_tb
def menu_links(request):
    links=District_tb.objects.all()
    return dict(links=links)