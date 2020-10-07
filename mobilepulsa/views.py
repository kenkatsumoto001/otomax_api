from django.shortcuts import render
import json

from . import get_data


def price_list(request, * args, **kwargs):
    datas = get_data.price_list()

    context = {
        'datas': datas,
    }
    return render(request, 'mobilepulsa/price_list.html', context)
