from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class ShopPageView(TemplateView): 
    template_name = 'shop.html'

class ProductPageView(TemplateView): 
    template_name = 'product.html'

class UsersPageView(TemplateView): 
    template_name = 'users.html'