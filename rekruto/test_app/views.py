from django.shortcuts import render

def index_page(request):
    '''
    if request.GET['name'] == None:
        name = 'Noname'
    else:
        name = request.GET['name']
    if request.GET['message'] == None:
        message = 'Тут что-то должно быть'
    else:
        message = request.GET['message']
    '''
    if request.GET:
        name = request.GET['name']
        message = request.GET['message']
    else:
        name = 'Noname'
        message = 'Тут что-то должно быть'
    return render(request, 'index.html', {'name':name, 'message':message})