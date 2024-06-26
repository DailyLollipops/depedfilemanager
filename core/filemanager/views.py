from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .models import Document
from .utils import paramutils

def home(request: HttpRequest):
    documents = Document.objects.all()
    context = {
        'documents': documents,
        'query': '',
        'category': 'all',
        'communication': 'all',
    }
    return render(request, 'home.html', context=context)



def search(request: HttpRequest):
    params = ['query', 'category', 'communication']
    if not paramutils.validate_params(request.GET, params):
        return redirect('/filemanager')
    
    query = request.GET.get('query')
    category = request.GET.get('category')
    communication = request.GET.get('communication')

    documents = Document.objects.all()
    if query:
        documents = documents.filter(
            Q(name__icontains=query) | 
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    if category and category != 'all':
        documents = documents.filter(category__exact=category)
    if communication and communication != 'all':
        documents = documents.filter(communication__exact=communication)

    context = {
        'documents': documents,
        'query': query,
        'category': category,
        'communication': communication,
    }
    return render(request, 'home.html', context=context)



def get(request: HttpRequest):
    params = ['id']
    
    if not paramutils.validate_params(request.GET, params):
        return JsonResponse({
            'success': False,
            'message': 'Missing parameter'
        })

    id = request.GET.get('id')

    try:
        document = Document.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Document does not exist'
        })
    
    data = {
        'success': True,
        'id': document.id,
        'name': document.name,
        'title': document.title,
        'category': document.category,
        'communication': document.communication,
        'description': document.description,
        'file': document.file.url
    }
    return JsonResponse(data)



@requires_csrf_token
def add(request: HttpRequest):
    details = request.POST.dict()
    params = ['name', 'title', 'category', 'communication', 'description']

    if not paramutils.validate_params(details, params):
        return JsonResponse({
            'success': False,
            'message': 'Missing parameter'
        })

    name = details.get('name')
    title = details.get('title')
    category = details.get('category')
    communication = details.get('communication')
    description = details.get('description')
    file = request.FILES.get('file')

    if not file:
        return JsonResponse({
            'success': False,
            'message': 'Missing parameter'
        })
    
    data = {
        'name': name,
        'title': title,
        'category': category,
        'communication': communication,
        'description': description,
        'file': file
    }
    document = Document(**data)
    document.save()
    return redirect('/filemanager')



@requires_csrf_token
def edit(request: HttpRequest):
    details = request.POST.dict()
    params = ['id', 'name', 'title', 'category', 'communication', 'description']

    if not paramutils.validate_params(details, params):
        return JsonResponse({
            'success': False,
            'message': 'Missing parameter'
        })
    
    id = details.get('id')
    name = details.get('name')
    title = details.get('title')
    category = details.get('category')
    communication = details.get('communication')
    description = details.get('description')
    
    try:
        document = Document.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Document does not exist'
        })
    
    document.name = name
    document.title = title
    document.category = category
    document.communication = communication
    document.description = description
    document.save()
    return redirect('/filemanager')



@requires_csrf_token
def delete(request: HttpRequest):
    details = request.POST.dict()
    params = ['id']

    if not paramutils.validate_params(details, params):
        return JsonResponse({
            'success': False,
            'message': 'Missing parameter'
        })
    
    id = details.get('id')
    
    try:
        document = Document.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Document does not exist'
        })
    
    document.delete()
    return redirect('/filemanager')
