import math

def calc_sorting(request):
  return {
    "sort_enabled": 1 if request.GET.get("sort") is not None else 0,
    "asc": 1 if request.GET.get("sort_order") == "asc" else 0,
    "desc": 1 if request.GET.get("sort_order") == "desc" else 0
  }


def get_url_page(request):
  if request.GET.get("page") and request.GET.get("page").isnumeric():
    return request.GET.get("page")
  else:
    return 1


def calc_pagination(entries, ITEMS_PER_PAGE, current_page):
  return {
    "entries_amount": len(entries),
    "pages_amount": math.ceil(len(entries) / ITEMS_PER_PAGE),
    "items_per_page": ITEMS_PER_PAGE,
    "current_page": current_page,
    "next_page": int(current_page) + 1,
    "prev_page": int(current_page) - 1 if int(current_page) > 1 else 1
  }
