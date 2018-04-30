from django.shortcuts import render_to_response, get_object_or_404
from .models import Article

# Create your views here.


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = dict()
    context['article_obj'] = article
    return render_to_response("article_detail.html", context)
    # return HttpResponse("文章: %s" % article.title)

def article_list(request):
    # articles = Article.objects.all()
    articles = Article.objects.filter(is_deleted=False)
    context = dict()
    context['article_list'] = articles
    return render_to_response("article_list.html", context)
