from django.http import HttpResponse
import datetime
from django.shortcuts  import render

def home(request):
    date=datetime.datetime.now()  
    print("This is Home page of my website")
    return render(request,'home.html',{})
    
def about(request):
    print("you van see that the view is succesfuly diplayed on about page")
    return HttpResponse("<h1> hellow this is about us page</h1>")

def profile(request):
    date=datetime.datetime.now()  
    print("This is Home page of my website")
    return render(request,'about.html',{})

def services(request):
    date=datetime.datetime.now()  
    isactive="True"
    servicename="Breakfats ! Lunch ! Dinner"
    # suppose we have some list of programs
    list_of_programs=[
        'wap to find even or odd',
        'wap to check prime numbers',
        'wap tp rint all prime numbers from 1 to 100'
    ]
# lets create a dictionary that is having key - value pair
    hotelservices={'hotelname':"Ashoka", 'Owner':"Sr. Ratan Tata"} 
    # print("This is Services  page of my website",{isactive})
    # now putting all these dynamic data into a single dictionary so that we can render i
    #render it on services.html page 
    globaldictionary={
        'date':date,
        'isactive':isactive,
        'servicename':servicename,
        'list_of_programs':list_of_programs,
        'hotelservices':hotelservices
        
    }
    # passing this globadictionary do that aal dynaic data can be passed as keys
    return render(request,"services.html" ,globaldictionary)

def sample(request):
    date=datetime.datetime.now()  
    print("This is Services  page of my website")
    #return HttpResponse("<h1> hellow this is Home page </h1>"+str(date))
    return render(request,"services.html", {'student':'student'})   

    # Function to return HTML Template uisng render but we need to import it as well

# sending dynaic data to the template html 
def dynamic(request):
    # creating a dictionary : to render a dynamic data we always create a ductionary 
    data={'title':'This is Home page','name':'Dr. Mukesh Mann','college':'IIITSonepat'}
    return render (request,'dynamic.html', data)


def forloop(request):
    date=datetime.datetime.now()  
    isactive="True"
    servicename="Breakfats ! Lunch ! Dinner"
    # suppose we have some list of programs
    list_of_programs=[
        'wap to find even or odd',
        'wap to check prime numbers',
        'wap tp rint all prime numbers from 1 to 100'
    ]
# lets create a dictionary that is having key - value pair
    hotelservices={'hotelname':"Ashoka", 'Owner':"Sr. Ratan Tata"} 
    listofhotels=[{'name':'XYZ','owner':'ram'},
    {'name':'pqr','owner':'Mukesh'},
    {'name':'sss','owner':'Sunny'}]
    # print("This is Services  page of my website",{isactive})
    # now putting all these dynamic data into a single dictionary so that we can render i
    #render it on services.html page 
    globaldictionary={
        'date':date,
        'isactive':isactive,
        'servicename':servicename,
        'list_of_programs':list_of_programs,
        'hotelservices':hotelservices,
        'listofhotels': listofhotels
        
    }
    # passing this globadictionary do that aal dynaic data can be passed as keys
    return render(request,"forloop.html" ,globaldictionary)

   
def ifeslelogic(request):
    # creating a dictionary : to render a dynamic data we always create a ductionary 
    mydictionary=[{'name':'Mukesh','mobile':30},
                 {'name':'Rakesh','mobile':40},
                 {'name':'Ram','mobile':50}]
    Mylist=[100,200,300]
    globaldictionary={'title':'This is Home page',
                 'name':'Dr. Mukesh Mann',
                 'college':'IIITSonepat',
                 'mydictionary':mydictionary,
                 'list': [20,30,40],
                 'Mylsit':Mylist}
    # Sending Global dictionary hence all things contained in globaldictionary is now 
    # available on ifelse.html page, you can use this now
    return render (request,'ifeslelogic.html', globaldictionary)

    # Dynamic Urls
def coursedetails(request,courseid):
    return HttpResponse(courseid)

def indexpage(request):
    return render(request,'index.html')


        
