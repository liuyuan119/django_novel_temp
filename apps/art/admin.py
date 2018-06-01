# from django.contrib import admin

# Register your models here.
from art.models import Art, Tag
import xadmin
from xadmin import views


class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 整体配置
    site_title = '美文后台管理系统'
    site_footer = 'python项目'
    menu_style = 'accordion'  # 菜单折叠


class TagAdmin(object):
    # 后台列表显示列
    list_display = ['t_name', 't_info', 't_createtime']
    # 后台列表查询条件
    search_fields = ['t_name', 't_createtime']
    # 后台列表通过时间查询
    list_filter = ['t_name', 't_info', 't_createtime']
    list_per_page = 10


class ArtAdmin(object):
    # 后台列表显示列
    list_display = ['a_title', 'a_info', 'a_content', 'a_img', 'a_addtime', 'a_updatetime']
    # 后台列表查询条件
    search_fields = ['a_title', 'a_info', 'a_content']
    # 后台列表通过时间查询
    list_filter = ['a_title', 'a_info', 'a_content', 'a_addtime']
    list_per_page = 20
    style_fields = {'a_content': 'ueditor'}


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Art, ArtAdmin)
