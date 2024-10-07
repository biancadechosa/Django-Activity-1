# views.py
from django.shortcuts import render

# Dummy data for demonstration
products = [
    {'id': 1, 'name': 'Chocolate Cake', 'description': 'Indulge in the rich, decadent experience of our chocolate cake, a timeless classic that never fails to impress. This moist and fluffy cake is made from high-quality cocoa powder, ensuring a deep chocolate flavor in every bite. Its luscious layers are perfectly complemented by a velvety chocolate ganache or creamy frosting, which adds a smooth, sweet finish. Topped with chocolate shavings or sprinkles, each slice is a work of art that’s perfect for any celebration—be it birthdays, weddings, or just a sweet treat to enjoy. Serve it with a scoop of vanilla ice cream or a dollop of whipped cream for an extra touch of indulgence. Dive into a slice of happiness that is sure to satisfy your chocolate cravings!', 'price': 1500, 'image_url': 'http://127.0.0.1:8000/static/images/chocolate_cake.jpeg'},
    {'id': 2, 'name': 'Strawberry Cake', 'description': 'Experience the fresh, vibrant taste of our strawberry cake, a delightful dessert that captures the essence of summer in every bite. This light and airy cake is crafted with tender vanilla layers infused with real strawberry puree, ensuring a burst of fruity flavor in every slice. Each layer is generously filled with a luscious strawberry frosting made from cream cheese and whipped cream, creating a harmonious balance of sweetness and tanginess. Topped with fresh, juicy strawberries and a sprinkle of powdered sugar, this cake is as beautiful as it is delicious. Perfect for celebrations, picnics, or simply as a sweet indulgence, our strawberry cake is a refreshing treat that will leave you craving more. Enjoy it chilled or at room temperature, and pair it with a dollop of whipped cream for the ultimate dessert experience!', 'price': 2000, 'image_url': 'http://127.0.0.1:8000/static/images/strawberry.png'},
    {'id': 3, 'name': 'Red Velvet Cake', 'description': 'Indulge in the rich, decadent experience of our red velvet cake, a timeless classic that promises to impress. This stunning cake features velvety layers of moist red velvet sponge, beautifully contrasted with a smooth and creamy cream cheese frosting that melts in your mouth. The subtle hint of cocoa adds depth to the flavor, while the vibrant red color creates a striking visual appeal that makes it a showstopper for any occasion. Each slice is a perfect blend of sweetness and tanginess, ensuring a delightful taste sensation with every bite. Perfect for birthdays, anniversaries, or any celebration, our red velvet cake is not just a dessert; it’s an experience that will leave your taste buds dancing with joy. Serve it chilled for an extra refreshing treat, and watch as it becomes the highlight of your dessert table!', 'price': 1200, 'image_url': 'http://127.0.0.1:8000/static/images/red_velvet.jpg'},
]

def index(request):
    return render(request, 'index.html')

def product_list(request):
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = next(p for p in products if p['id'] == product_id)
    return render(request, 'product_detail.html', {'product': product})
