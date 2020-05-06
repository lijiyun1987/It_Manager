from django import template
register = template.Library()
## 基于bootstrap的分页器
@register.simple_tag
def custom_paginator(page, num_total_pages=9, num_back_pages=3):

    html = ''
    if page.has_previous():
        html = '<li class ="page-item"> <a class ="page-link" href="?page=%s"><</a> </li>' % page.previous_page_number

    if page.paginator.num_pages <= num_total_pages:
        # 分页的总页数不超过10页，不考虑当前点击的页码是否是中心位置了：
        for x in page.paginator.page_range:
            if x == page.number:
                html += '<li class ="page-item active" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
            else:
                html += '<li class ="page-item" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
    elif page.number <= num_total_pages - num_back_pages:
        for x in range(1, num_total_pages):
            if x == page.number:
                html += '<li class ="page-item active" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
            else:
                html += '<li class ="page-item" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
        html += '<li class ="page-item"> <a class ="page-link" href="?page=%s">...</a></li>' % ((page.number + page.paginator.num_pages) // 2)
        html += '<li class ="page-item"> <a class ="page-link" href="?page=%s">%s</a></li>' % (page.paginator.num_pages, page.paginator.num_pages)
    # (num_total_pages - num_back_pages - 3):预定义当前选中页码前面是3个页码(不包含1和...)
    elif num_total_pages - (num_total_pages - num_back_pages - 3) <= page.number <= page.paginator.num_pages - num_back_pages:
        html += '<li class ="page-item"> <a class ="page-link" href="?page=1">1</a></li>'
        html += '<li class ="page-item"> <a class ="page-link" href="?page=%s">...</a></li>' % (page.number//2)
        # 1...2 3 4 5 6 7 8 9
        for x in range(page.number - (num_total_pages - num_back_pages - 3), page.number + num_back_pages + 1):
            if x == page.number:
                html += '<li class ="page-item active" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
            else:
                html += '<li class ="page-item" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
        html += '<li class ="page-item"> <a class ="page-link" href="?page=%s">...</a></li>' % ((page.number + page.paginator.num_pages) // 2)
        html += '<li class ="page-item"> <a class ="page-link" href="?page=%s">%s</a></li>' % (page.paginator.num_pages, page.paginator.num_pages)
    else:
        # 最后无法滚动的部分
        html += '<li class ="page-item"> <a class ="page-link" href="?page=1">1</a></li>'
        html += '<li class ="page-item"> <a class ="page-link" href="?page=%s">...</a></li>' % (page.number//2)
        for x in range(page.paginator.num_pages - (num_total_pages - num_back_pages - 3) - num_back_pages, page.paginator.num_pages + 1):
            if x == page.number:
                html += '<li class ="page-item active" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
            else:
                html += '<li class ="page-item" > <a class ="page-link" href="?page=%s">%s</a></li>' % (x, x)
    if page.has_next():
        html += '<li class ="page-item"> <a class ="page-link" href="?page=%s">></a> </li>' % page.next_page_number
    return html


