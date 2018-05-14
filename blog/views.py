from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.detail import DetailView
import markdown2, re
from blog.models import Article


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog(request):
    if request.method == 'GET':
        page_id = request.GET.get('page_id', 1)
        articles = Article.objects.all().order_by('-id')
        paginator = Paginator(articles, 3)
        articles_list = paginator.page(int(page_id))
        return render(request, 'blog.html', {'articles': articles_list})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.a_content = markdown2.markdown(obj.a_content)
        return obj


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')


def search(request):
    if request.method == 'GET':
        return render(request, 'search.html')


def search_for(request):
    search_for = request.GET['search_for']
    if search_for:
        results = []
        article_list = Article.objects.all().order_by('-id')
        for article in article_list:
            pattern = re.compile(search_for, flags=re.IGNORECASE)
            if pattern.findall(article.a_title):
                results.append(article)
        for article in results:
            article.body = markdown2.markdown(article.a_content)
        return render(request, 'search.html', {'arts': results})
    else:
        return render(request, 'search.html')


# def photo(request):
#     if request.method == 'GET':
#         page_id = request.GET.get('page_id', 1)
#         photos = Photo.objects.all().order_by('-id')
#         paginator = Paginator(photos, 9)
#         photo_list = paginator.page(int(page_id))
#         return render(request, 'photo.html', {'photos': photo_list})
