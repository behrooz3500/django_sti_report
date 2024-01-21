import json
from django.shortcuts import render

def home(request):
    test_data = {
        "ReceiptInfo": {
            "invoice_date": "1402/10/12",
            "invoice_code": "1001",
            "company_name": "بهروز و دوستان",
            "company_tel": "09150207215",
            "company_address": "مشهد، قاسم آباد",
            "person_name": "علی کریمی",
            "tel": "09308744204",
            "address": "مشهد، آزادشهر",
            "company_note": "be good",
            "items_sum": "250000",
            "discount": "100000",
            "tax": "5000",
            "total": "245000",
            "previous_payments": "0",
            "receipt_total": "245000"
        },
        "ReceiptItems":[
            {
                "product_name": "پفک نمکی",
                "item_quantity": "2",
                "item_total": "250000"
            },
            {
                "product_name": "پفک نمکی",
                "item_quantity": "8",
                "item_total": "850000"
            },
            {
                "product_name": "پفک نمکی",
                "item_quantity": "2",
                "item_total": "250000"
            },
            {
                "product_name": "پفک نمکی",
                "item_quantity": "2",
                "item_total": "250000"
            }
        ]
    }
    json_data = json.dumps(test_data)
    context = {"json_data": json_data}
    return render(request, 'viewer.html', context=context)

