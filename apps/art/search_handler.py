from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from art.models import Art


def SearchHandler(request):
    key = request.GET.get("key", "")  ##获取输入参数key对应的值，默认为空
    if key == "":
        return HttpResponseRedirect("/")
    else:
        page = request.GET.get("page", 1)
        page = int(page)
        # 查询数据，或操作
        art_sets = Art.objects.filter(Q(a_title__contains=str(key))
                                      | Q(a_content__contains=str(key))
                                      | Q(a_info__contains=str(key))).distinct()
        # 查询数据，与操作
        # mdict = {
        #    'a_title':str(key),
        #    'a_content':str(key)
        # }
        # Art.objects.filter(mdict)

        total = art_sets.count()
    shownum = 10
    import math
    pagenum = int(math.ceil(total / shownum))
    if page < 1:
        return HttpResponseRedirect(request.path + "?page=%d&key=%s" % (1, key))
    if page > pagenum:
        return HttpResponseRedirect(request.path + "?page=%d&key=%s" % (pagenum, key))
    offset = (page - 1) * shownum

    art_list = Art.objects.filter(Q(a_title__contains=str(key))
                                  | Q(a_content__contains=str(key))
                                  | Q(a_info__contains=str(key))).distinct()

    data = art_list[offset:(shownum + offset)]
    btnnum = 5
    if btnnum > pagenum:
        firstpage = 1
        lastpage = pagenum
    else:
        if page == 1:
            firstpage = 1
            lastpage = btnnum
        else:
            firstpage = page - 2
            lastpage = page + btnnum - 3
            if firstpage < 1:
                firstpage = 1
            if lastpage > pagenum:
                lastpage = pagenum
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
        pagerange=range(firstpage, lastpage + 1),
        data=data,
        url=request.path,
        key=key,
        page=page
    )
    return render(request, "home/search.html", context=context)
