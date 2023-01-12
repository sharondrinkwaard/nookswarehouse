from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


SIZE_CHOICES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
)

COLOR_CHOICES = (
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Orange', 'Orange'),
)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, blank=True, null=True)
    size_option = models.CharField(max_length=80, choices=SIZE_CHOICES, default='S')
    quantity = models.IntegerField(blank=False, default=1)
    has_color = models.BooleanField(default=False, blank=True, null=True)
    color_option = models.CharField(max_length=15, blank=True, default='Red', choices=COLOR_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class QuantitySize(models.Model):
    # Class which is used to create the form for the product_detail page
    # posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    size_option = models.CharField(max_length=80, choices=SIZE_CHOICES, default='S')
    
    def __str__(self):
        return f'Quantity: {self.quantity} | Size: {self.size_option}'
