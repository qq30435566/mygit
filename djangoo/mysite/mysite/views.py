from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World 123 456")