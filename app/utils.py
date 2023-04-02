from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.db.models import QuerySet


def replace_chars_in_query(string, to_be_replaced="iIlL1|"):
    if string[0] in to_be_replaced:
        string = "Ӏ" + string[1:]
    for i in to_be_replaced:
        if i in string:
            string = string.replace(i, "ӏ")
    return string


def create_paginator(object_list: QuerySet, request: WSGIRequest, per_page=30):
    paginator = Paginator(object_list, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj
