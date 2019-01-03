from django.shortcuts import render

def post_list(request):
    return render(request, 'webpage/post_list.html', {})
