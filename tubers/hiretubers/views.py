from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Hiretuber

# Create your views here.

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        user_id = request.POST['user_id']
        tuber_city = request.POST['tuber_city']
        tuber_price = request.POST['tuber_price']

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, phone=phone, city=city, state=state, message=message, tuber_id=tuber_id, tuber_name=tuber_name, user_id=user_id, tuber_city=tuber_city, tuber_price=tuber_price)
        hiretuber.save()
        messages.success(request, 'Thanks for reaching us!!!')
        return redirect('youtubers')
        
 



