from django.db import models
from ckeditor.fields import RichTextField

class Module(models.Model):

    module_choices = (
        ('Choose' ,'Choose'),
        ('1' ,'1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )

    module_id = models.AutoField
    module_options = models.CharField(max_length=50,choices = module_choices,default =module_choices[0][0],blank=False,null=False)
    module_numbering = models.CharField(max_length=5,blank=False,null=False)
    module_numbering_title = models.CharField(max_length=100,blank=False,null=False)
    module_subtitle_numbering = models.CharField(max_length=5,blank=False,null=False,default='-')
    module_numbering_subtitle  = models.CharField(max_length=500,blank=False,null=False,default='-')
    description = RichTextField(blank=False,null=False)
    drive_link = models.CharField(max_length=250,blank=False,null=False,default='#')


    def __str__(self):
        return self.module_numbering_title
