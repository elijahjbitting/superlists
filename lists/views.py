from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(req):
	return render(req,'home.html',{
		'new_item_text': req.POST.get('item_text','')
	} )
