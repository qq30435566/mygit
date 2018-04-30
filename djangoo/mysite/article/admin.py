from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author",
                    "create_time", "last_update_time",
                    "read_num", "is_deleted", )
    ordering = ("-id",)  # 按id倒叙排列, '-' 表示倒叙

# admin.site.register(Article, ArticleAdmin)
# @admin.register(Article)是上面一行的装饰器写法
