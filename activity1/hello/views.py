from django.shortcuts import render

# Dummy data for demonstration
cars = [
    {'id': 1, 'name': 'Toyota Camry', 'description': 'The Toyota Camry is a spacious midsize sedan that is known for its reliability and fuel efficiency. With a comfortable interior and a smooth ride, the Camry is perfect for both daily commutes and long road trips. Its advanced safety features and cutting-edge technology make it a favorite among families and individuals alike.', 'price': 2500000, 'image_url': 'http://127.0.0.1:8000/static/images/car1.jpg'},
    {'id': 2, 'name': 'Honda Civic', 'description': 'The Honda Civic is a compact car that combines sporty performance with practicality. With its sleek design and efficient engine, the Civic offers a fun driving experience while also being economical. It features a modern interior packed with tech-savvy features and ample cargo space, making it a top choice for young professionals and families.', 'price': 2200000, 'image_url': 'http://127.0.0.1:8000/static/images/car2.jpg'},
    {'id': 3, 'name': 'Ford Mustang', 'description': 'The Ford Mustang is an iconic American muscle car that exudes power and style. With its powerful engine options and sharp handling, the Mustang delivers an exhilarating driving experience. Its aggressive design, comfortable seating, and advanced technology make it a standout choice for car enthusiasts and those looking for a thrilling ride.', 'price': 3000000, 'image_url': 'http://127.0.0.1:8000/static/images/car3.jfif'},
]

def home(request):
    return render(request, 'home.html')

def car_list(request):
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = next(c for c in cars if c['id'] == car_id)
    return render(request, 'car_detail.html', {'car': car})

