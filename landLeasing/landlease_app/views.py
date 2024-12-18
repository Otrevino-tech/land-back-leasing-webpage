from django.shortcuts import render


def __client_helper(): 
    print("TODO")

def __admin_helper(): 
    print("TODO")

# homes for landing page 
def client_home(request):
    __client_helper()
    return render(request, "client/home.html", {})

def admin_home(request):  
    __client_helper()
    return render(request, "admin/home.html", {})

# Client
def client_cart(request): 
    __client_helper()
    return render(request, "client/cart.html")

def client_about(request): 
    __client_helper()
    return render(request, "client/about.html")

def client_profile(request): 
    __client_helper()
    return render(request, "client/profile.html")

def client_login(request): 
    __client_helper()
    return render(request, "client/login.html")

def client_register(request): 
    __client_helper()
    return render(request, "client/register.html")

# admin
def admin_cart(request): 
    __admin_helper()
    return render(request, "admin/cart.html")

def  admin_about(request): 
    __admin_helper()
    return render(request, "admin/about.html")

def admin_profile(request): 
    __admin_helper()
    return render(request, "admin/profile.html")

def admin_login(request): 
    __admin_helper()
    return render(request, "admin/login.html")

def admin_register(request): 
    __admin_helper()
    return render(request, "admin/register.html")
