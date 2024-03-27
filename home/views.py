from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.8

def home(request):
    peoples = [
        {'name' : 'Tejas Gorule','age': 23},
        {'name' : 'Nishant Dhuri','age': 28},
        {'name' : 'Nishant Desai','age': 24},
        {'name' : 'Akshay velam','age': 29},
        {'name' : 'Vipul Rewale','age': 13}
    ]
    
    text= "Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur adipisci distinctio ea! Possimus ex non quibusdam quo quae. Tempora velit dolor voluptate aspernatur corporis corrupti, doloribus quae assumenda cumque, eaque nobis harum delectus nam id praesentium. Molestias, aperiam velit esse, perspiciatis necessitatibus nulla alias hic suscipit, unde fuga voluptatibus ratione. Consequuntur, odit eum. Optio aliquid, labore atque earum nisi dignissimos minus, deserunt temporibus delectus placeat voluptatibus! Excepturi ducimus eveniet omnis corrupti illo, praesentium repellendus eius, provident ad harum quam aperiam dignissimos quos ullam labore. Expedita soluta quia alias obcaecati nostrum totam sit quos architecto ad delectus debitis officiis, explicabo deleniti."
    veg = ['yee','eedd','effs','ffef8']
    return render(request,"index.html",context={'page': 'home' ,'peoples':peoples,'veg':veg})


# def home(request):
#     return HttpResponse("<h1 >Hey I am tejass</h1>")

def about(request):
    context = {'page': 'about'}
    return render(request,"about.html",context)

def contact(request):
    context = {'page': 'contact'}
    return render(request,"contact.html",context)

def landing_page(request):
    return HttpResponse("<h1>This is landing page8</h1>")
