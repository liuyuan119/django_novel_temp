from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# Create your views here.
from art.models import Art, Tag
from django_novel.settings import logger
import json


def IndexHandler(request):
    # 基础默认信息
    #
    logger.info("IndexHandler request Handler begin")
    url = request.path
    page = int(request.GET.get("page", 1))
    t = int(request.GET.get("t", 0))
    if request.method == "POST":
        page = request.POST.get("page")
        if page.isdigit():
            page = int(page)
        else:
            page = 1
    if t == 0:
        total = Art.objects.all().count()
    else:
        total = Art.objects.filter(a_tag_id=t).count()
    #
    logger.debug('query total:' + str(total))
    tags = Tag.objects.all()
    context = dict(
        pagenum=1,
        total=1,
        prev=1,
        next=1,
        pagerange=range(1, 2),
        data=[],
        url=url,
        tags=tags,
        page=1,
        t=0
    )
    if total > 0:
        import math
        show_num = 1
        pagenum = math.ceil(total / show_num)
        if page < 1:
            url = url + "?page=1&t=%s" % t
            return HttpResponseRedirect(url)
        if page > pagenum:
            url = url + "?page=%s&t=%s" % (pagenum, t)
            return HttpResponseRedirect(url)
        offset = (page - 1) * show_num
        if t == 0:
            data = Art.objects.all()[offset:offset + show_num]
        else:
            data = Art.objects.filter(a_tag_id=t)[offset:offset + show_num]
        btnnum = 5
        if btnnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            # 用btnnum 来卡 中间部分直接就是这样
            # 分情况讨论 firstpage小于1 firstpage-lastpage 整体大于1 --此时前端显示区间是(first, last)
            # 分情况讨论 lastpage大于pagenum firstpage-lastpage 整体小于page总数pagenum --此时是(first+1, last+1) 因为右边闭区间
            firstpage = page - btnnum // 2
            lastpage = page + (btnnum - btnnum // 2)
            if firstpage < 1:
                lastpage = lastpage + (1 - firstpage)
                firstpage = 1
            if lastpage > pagenum:
                firstpage = firstpage - (lastpage - pagenum) + 1
                lastpage = pagenum + 1
        prev = page - 1
        next = page + 1
        if prev < 1:
            prev = 1
        if next > pagenum:
            next = pagenum
        context = dict(
            pagenum=pagenum,
            total=total,
            prev=prev,
            next=next,
            pagerange=range(firstpage, lastpage),
            data=data,
            url=url,
            tags=tags,
            page=page,
            t=t
        )
    return render(request, 'home/index.html', context=context)


def add_handler(request):
    x = request.GET.get('x', '1')
    y = request.GET.get('y', '1')
    from .tasks import add
    add.delay(int(x), int(y))
    res = {'code': 200, 'message': 'ok', 'data': [{'x': x, 'y': y}]}
    return HttpResponse(json.dumps(res))
# from django_novel.settings import logger
#
# def test():
#     logger.info("info msg")
#     logger.debug("debug msg")
#     print(1)
#
# test()
