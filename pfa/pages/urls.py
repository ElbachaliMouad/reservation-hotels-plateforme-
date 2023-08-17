from django.urls import path 
from . import views 
urlpatterns=[

    path('',views.index,name='index'),

    path('about',views.about,name='about'),

    path('contact',views.contact,name='contact'),

    path('signin',views.signin,name='signin'),

    path('signup',views.signup,name='signup'),

    path('clone',views.clone,name='clone'),

    path('bibliotheque',views.bibliotheque,name='bibliotheque'),

    path('explore2',views.explore2,name='explore'),

    path('visitornavi',views.visitornavi,name='visitornavi'),
 
    path('activitemain',views.activitemain,name='activitemain'),

    path('activite',views.activite,name='activite'),

    path('bibliotheque2',views.bibliotheque2,name='bibliotheque2'),

    path('demand',views.demand,name='demand'),

    path('detailimages',views.detailimages,name='detailimages'),

    path('explore2',views.explore2,name='explore2'),

    path('galeryactivite',views.galeryactivite,name='galeryactivite'),

    path('main',views.main,name='main'),

    path('mediaworkshop',views.mediaworkshop,name='mediaworkshop'),

    path('message',views.message,name='message'),

    path('notification',views.notification,name='notification'),

    path('profiles',views.profiles,name='profiles'),

    path('settingprofiles',views.settingprofiles,name='settingprofiles'),

    path('settingworkshop',views.settingworkshop,name='settingworkshop'),
   
    path('workshop',views.workshop,name='workshop'),
    
    path('workshopmain',views.workshopmain,name='workshopmain'),
   
    path('workshopmembre',views.workshopmembre,name='workshopmembre'),
    

    path('workshopmembre2',views.workshopmembre2,name='workshopmembre2'),

    
     path('log_out',views.log_out, name='log_out'),

    path('delete_image/<int:workshop_id>/', views.delete_image, name='delete_image'),

    path('list_workshop/<int:workshop_id>',views.list_workshop, name='list_workshop'),

    path('searchresult',views.searchresult,name='searchresult'),


]