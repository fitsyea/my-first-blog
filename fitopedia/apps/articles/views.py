from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog.html', {})

#def index(request):
#	return HttpResponse("Ну, я пытаюсь")