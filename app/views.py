from django.shortcuts import render
# for email stuff
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        shedule = request.POST['shedule']
        time = request.POST['time']
        message = request.POST['message']

        appointment = 'name:'+name+'phone:'+phone+'/ email:'+email+'/ address:'+address+'/ shedule:'+shedule+'/ time:'+time+'/ shedule:'+message

        # sending mail
        send_mail(
            'appointment request', #subject
            appointment, #message
            email, #from email
            ['rehmanzzulfiqar0@gmail.com']  #to email
            #for more than one put a coma
        )

        return render(request, 'home.html', {
            'name':name,
            'phone':phone,
            'email':email,
            'address':address,
            'shedule':shedule,
            'time':time,
            'message':message
        })
    else:
        return render(request, 'home.html')
        
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # sending mail
        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['rehmanzzulfiqar0@gmail.com']  #to email
            #for more than one put a coma
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def services(request):
    return render(request, 'services.html', {})

def about(request):
    return render(request, 'about.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def review(request):
    return render(request, 'review.html', {})

def blogs(request):
    return render(request, 'blogs.html', {})

    
  