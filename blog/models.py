from django.db import models

# Create your models here.
class blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    head0 = models.CharField(max_length=5000, default='')
    contenthead = models.TextField(max_length=5000, default='')
    head1 = models.CharField(max_length=100)
    contenthead1 = models.TextField(max_length=500, default='')
    head2 = models.CharField(max_length=100)
    contenthead2 = models.TextField(max_length=5000, default='')
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.title  # Fixed indentation issue
