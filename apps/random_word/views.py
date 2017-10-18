from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# unique_id = get_random_string(length=14)
# unique_id
# u'rRXVe68NO7m3mHoBS488KdHaqQPD6Ofv'

  # the index function is called when root is visited

def index(request):
    
    if 'unique_id' not in request.session:
       request.session['unique_id']=""
    if 'count' not in request.session:
       request.session['count'] = 0
    return render(request,'random_word/index.html')

def generate(request):
    unique_id = get_random_string(length=14)
    print "in generate"
    request.session['count']+=1
    print request.session['count']
    request.session['unique_id'] = unique_id
    # return render(request, "random_word/index.html",request.session['count'])    
    return redirect('/')



def reset(request):
    del request.session['count']
    del request.session['unique_id']
    return redirect('/')