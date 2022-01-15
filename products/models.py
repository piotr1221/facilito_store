from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    # auto_add_now agrega el campo automaticamente
    created_at = models.DateTimeField(auto_now_add=True)

    # una forma de crear el slug previo a su creacion es
    # sobreescribiendo la funcion save()
    
    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super(Product, self).save(*args, **kwargs)

    # Sin embargo, alternativa ideal seria usar callbacks, mas abajo
    

    def __str__(self):
        return self.title

# funcion callback
def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )
        instance.slug = slug

# antes de que un objeto se guarde en bd,
# se ejecutara el callback indicado
pre_save.connect(set_slug, sender=Product)