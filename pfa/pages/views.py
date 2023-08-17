from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from django.db.models import Q
from django.core.validators import validate_email
from django.contrib.auth.models import User 
from django.http import HttpResponse
from .models import Invitation
from .models import Workshop
from django.core.validators import validate_email
from .models import Membre
from .models import Picture
import hashlib

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import pages.serializers 

def index(request):

    return render(request,'pages/index.html')
    
def about(request):
    return render(request,'pages/about.html')


def contact(request):
    return render(request,'pages/contact.html')


def signin(request):
    error=False
    valid=False
    message1=""
    message=""
    if request.method =="POST":
        mail=request.POST.get('mail', None)
        password=request.POST.get('password', None)
        try :
            validate_email(mail)==False
        except:
            error=True
            message="Enter a valid email !"



        print("=="*5, "NEW POST:", mail, "=="*5)
        print("=="*5, "NEW POST:", password, "=="*5)
  

        user=User.objects.filter(email=mail).first()
        if user:
            user_mail=authenticate(username=user.username, password=password)
            if user_mail:
                membre=Membre.objects.filter(email=mail).first()
                print(user_mail.password, user_mail.email , membre.description)
                login(request, user_mail)
                return redirect('main')
            else: 
                error=True
                message="The password is incorect"
        
        else:
            error=True
            message="The email is wrong"
        








    context= {
        'error':error,
        'message':message,
        'valid': valid
    }
    
    return render(request,'pages/signin.html',context)

def signup(request):
    error=False
    valid=False
    message1=""
    message=""
    if request.method =="POST":
        username=request.POST.get('username', None)
        mail=request.POST.get('mail', None)
        password=request.POST.get('password', None)
        repassword=request.POST.get('repassword', None)
        invitation_code=request.POST.get('invitation_code',None)
        try :
            validate_email(mail)==False
        except:
            error=True
            message="Enter a valid email !"

        if error==False :
           if  password != repassword :
               error=True
               message="The two passwords are not the same !"
                   
        invi=Invitation.objects.filter(code=invitation_code).first()
        user=User.objects.filter( email=mail ).first()
      

        if user:
            error=True
            message= f"A user with existing {mail}  mail  !"
           
        
        if not invi:
            error=True
            message=f" Invitation code is wrong !"


        if invi  :
            value = invi.valeur     
            valid=True
            if value==1:
                message1=f"You are a Supervisor "
                type_user=1
                des='Supervisor'

            if value==0:
                message1=f"You are a membre "
                type_user=0
                des='Membre'



        if error == False and valid==True :
              
            membre=Membre(
                username=username,
                email=mail,
                type=type_user,
                code_invitation=invitation_code,
                description=des,
                
            
                
                  )
            membre.save()
            membre.password=password
            membre.save()
            invi.delete()

        
        if error == False and valid==True :
            user=User(
                username=username,
                email=mail,)

            user.save()
            user.password=password
            user.set_password(user.password)
            user.save()
          
            return redirect('signin')
            

            print("=="*5, "NEW POST:", username, "=="*5)
            print("=="*5, "NEW POST:", mail, "=="*5)
            print("=="*5, "NEW POST:", password, "=="*5)
            print("=="*5, "NEW POST:", repassword, "=="*5)
            print("=="*5, "NEW POST:", invitation_code, "=="*5)
        

        
        # form=UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     name=form.cleaned.data.get('First_Name')
        #     message.succes(request,f'Hi {name} your account was created succefully')
            # return redirect ('signin') 
        
    # else:
    #     form=UserCreationForm()

    context= {
        'error':error,
        'message':message,
        'message1':message1,
        'valid': valid
    }
    return render(request,'pages/signup.html',context)


def clone(request): 
    images=Workshop.objects.all()
    {'images':images}
    return render(request,'visitors/clone.html',{'images':images})

def visitornavi(request):

    return render(request,'visitors/visitornavi.html' )

def bibliotheque(request):
    return render(request,'visitors/bibliotheque.html')



@login_required(login_url='signin')
def activitemain(request):
    return render(request,'membre/activitemain.html')


@login_required(login_url='signin', )
def activite(request):
    return render(request,'membre/activite.html')

@login_required(login_url='signin')
def bibliotheque2(request):
    return render(request,'membre/bibliotheque2.html')



@login_required(login_url='signin')
def demand(request):
    return render(request,'membre/demand.html')



@login_required(login_url='signin')
def explore2(request):
    print('hey')
    error=False
    current_user = request.user
    if request.method =="POST":
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        image = request.FILES.get('image', None)
        image_content = request.FILES.get('image').read()
        image_hash = hashlib.md5(image_content).hexdigest()

        print("=="*5, "NEW POST:", title, "=="*5)
        print("=="*5, "NEW POST:", description, "=="*5)
        print("=="*5, "NEW POST:", image, "=="*5)
        if  not Picture.objects.filter(image_hash=image_hash).exists():
            
           Picture.objects.create(owner=request.user, image=image, description=description, title=title)



    pictures = Picture.objects.all()
 
    context= {'pictures': pictures,
             }

    return render(request,'membre/explore2.html', context)






@login_required(login_url='signin')
def galeryactivite(request):
    return render(request,'membre/galeryactivite.html')


@login_required(login_url='signin')
def main(request):
    images=Workshop.objects.all()
    {'images':images}
    return render(request,'membre/main.html',{'images':images})
    


@login_required(login_url='signin')
def detailimages(request):
    return render(request,'membre/detailimages.html')

@login_required(login_url='signin')
def mediaworkshop(request):
    return render(request,'membre/mediaworkshop.html')


@login_required(login_url='signin')
def message(request):
    connecteds=User.objects.all()
    
    return render(request,'membre/message.html', {'connecteds':connecteds})



@login_required(login_url='signin')
def notification(request):
    return render(request,'membre/notification.html')


@login_required(login_url='signin')
def profiles(request):

    current_user = request.user
    membre=Membre.objects.filter( username=current_user.username ).first()
    description=membre.description
    workshops = Workshop.objects.filter(owner=request.user)


    context={'description':description, 'workshops':workshops}
    return render(request,'membre/profiles.html',context)






@login_required(login_url='signin')
def settingprofiles(request):

    return render(request,'membre/settingprofiles.html')



@login_required(login_url='signin')
def settingworkshop(request):
    return render(request,'membre/settingworkshop.html' )



@login_required(login_url='signin')
def workshop(request):
    print('hey')
    error=True
    current_user = request.user
    membre=Membre.objects.filter( username=current_user.username ).first()
    description=membre.description
    if request.method =="POST":
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        image = request.FILES.get('image', None)
        print("=="*5, "NEW POST:", name, "=="*5)
        print("=="*5, "NEW POST:", description, "=="*5)
        print("=="*5, "NEW POST:", image, "=="*5)
        Workshop.objects.create(owner=request.user, image=image, description=description, name=name)

    workshops = Workshop.objects.filter(owner=request.user)
    if description=='supervisor':
        error=False
    context= {'workshops': workshops,
             'error': error
             }
    return render(request, 'membre/workshop.html',context)





@login_required(login_url='signin')
def workshopmain(request):
    return render(request,'membre/workshopmain.html')


@login_required(login_url='signin')
def workshopmembre(request):
    return render(request,'membre/workshopmembre.html')

@login_required(login_url='signin')
def workshopmembre2(request):
        return render(request,'membre/workshopmembre2.html')


@login_required(login_url='signin')

def delete_image(request, workshop_id ):
    image = get_object_or_404(Workshop, id=workshop_id, owner=request.user)
    print(image.name)
    image.delete()
    return redirect('workshop')

@login_required(login_url='signin')


def searchresult(request):
   

    workshops=Workshop.objects.all()

    return render(request,'membre/searchresult.html',{'workshops':workshops})





def list_workshop(request):
    return render(request,' membre/searchresult.html')


                   
def log_out(request):
    logout(request)
    return redirect('index')
