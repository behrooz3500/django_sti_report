import json
from django.shortcuts import render

test_data = {
        "ReceiptInfo": {
    	"address": "مشهد، آزادشهر",
		"carry_price": "15000",
        "courier_name": "peyke motori",
        "courier_tel": "091011011010",
    	"company_address": "مشهد، آدرس شرکت اینجاست",
    	"company_name": "بهروز و دوستان",
    	"company_note": "be good",
    	"company_tel": "09150207215",
    	"discount": "100000",
		"info": "اطلاعات اضافه",
		"invoice_code": "1001",
    	"invoice_date": "1402/10/12",
		"invoice_time": "12:45",
		"items_quantity": "5",
    	"items_sum": "250000",
		"logo_path": "/reports/logo.jpg",
		"order_place": "بیرون سالن",
		"person_code": "20035",
    	"person_name": "علی کریمی",
		"persons_number": "7",
    	"previous_payments": "0",
		"purchase_profit": "1000",
    	"receipt_total": "245000",
		"remain": "5000",
    	"tax": "5000",
    	"tel": "09308744204",
    	"total": "245000",
		"username": "آقای خاص"
    },
    "ReceiptItems":[
		{
			"item_info": "آبدار",
			"item_price": "12500",
			"item_quantity": "2",
			"item_total": "250000",
			"product_name": "1پفک نمکی",
			"discounted_price": "9500"
		},
		{
			"item_info": "آبدار",
			"item_price": "12500",
			"item_quantity": "4",
			"item_total": "250000",
			"product_name": "پفک نمکی",
			"discounted_price": "9500"
		},
		{
			"item_info": "آبدار",
			"item_price": "12500",
			"item_quantity": "6",
			"item_total": "250000",
			"product_name": "2پفک نمکی",
			"discounted_price": "9500"
		},
		{
			"item_info": "آبدار",
			"item_price": "12500",
			"item_quantity": "2",
			"item_total": "250000",
			"product_name": "3پفک نمکی",
			"discounted_price": "9500"
		},
		{
			"item_info": "آبدار",
			"item_price": "12500",
			"item_quantity": "2",
			"item_total": "250000",
			"product_name": "4پفک نمکی",
			"discounted_price": "9500"
		}
    ]
    }

def home(request):
    return render(request, 'index.html')

def single_viewer(request):
    json_data = json.dumps(test_data)
    context = {"json_data": json_data}
    return render(request, 'single_viewer.html', context=context)

def dynamic_viewer(request):
    json_data = json.dumps(test_data)
    context = {"json_data": json_data}
    return render(request, 'dynamic_viewer.html', context=context)

