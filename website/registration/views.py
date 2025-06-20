from django.shortcuts import render

# Create your views here.


def index (request) : 
    data = {
        'title' : 'Главная страница' , 
        'values' : ['123' , '52', 'чиназес']
    }
    return render (request  , 'registration/index.html'  , data)

def about (request) : 
    data = {
        'title' : 'Про нас'
    }
        
    
    return render (request , 'registration/about.html' , data )
