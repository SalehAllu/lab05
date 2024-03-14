from django.shortcuts import render, redirect

# Person class
class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

# List to store Person instances
people = []

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username, password)
        people.append(person)
        return redirect('/')
    return render(request, 'add.html')

def index(request):
    return render(request, 'index.html', {'people': people})
