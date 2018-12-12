from django.shortcuts import render

from .models import Tweet
# Create your views here.

#retrive
def tweet_detail_view(request, id=1):
	obj = Tweet.objects.get(id=1)
	print(obj)
	context = {
	"objects": obj
	}
	return render (request, "tweets/detail_view.html", context)

def tweet_list_view(request):
	queryset = Tweet.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.content)
		context = {
		"objects_list": queryset
		}
	return render (request, "tweets/list_view.html", context)