def calc_sort(request):
  return {
    'no_sort': 1 if request.GET.get('sort') is not None else 0,
    'asc': 1 if request.GET.get('sort_order') == 'asc' else 0,
    'desc': 1 if request.GET.get('sort_order') == 'desc' else 0
  }


def get_url(request):
  if request.GET.get('page') and request.GET.get('page').isnumeric():
    return request.GET.get('page')
  return 1


def calc_total_pages(entries, per_page):
  return len(entries) // per_page if len(entries) % per_page == 0 else len(entries) // per_page + 1


def calc_pages(entries, per_page):
    return len(entries) // per_page if len(entries) % per_page == 0 else len(entries) // per_page + 1


def calc_pagi(entries, per_page, cur_page):
    return {
        'entries':len(entries),
        'pages': calc_pages(entries, per_page),
        'per_page':per_page,
        'cur_page':cur_page,
        'next':int(cur_page)+1 if int(cur_page) < calc_pages(entries, per_page) else int(cur_page),
        'prev':int(cur_page)-1 if int(cur_page)>1 else 1
    }
