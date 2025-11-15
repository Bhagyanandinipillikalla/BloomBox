from django.db import models

# Create your models here.
class Plant(models.Model):
    Choice= [
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
        ("Medicinal", "Medicinal"),
        ("Flowering", "Flowering"),
    ]
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50, choices=Choice)
    price=models.FloatField()
    about=models.TextField() 
    image=models.ImageField(upload_to="images/")
    discount_percent=models.IntegerField(null=True)


    def final_price(self):
        if self.discount_percent:
            amount=(self.price*self.discount_percent)/100
            return int(self.price-amount)
        return self.price
