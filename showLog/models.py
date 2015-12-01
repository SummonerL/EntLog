from django.db import models

# Create your models here.

#Entry model - An entry in our entertainment log
class Entry(models.Model):
    ENTERTAINMENT_TYPES = (
        ('BO', 'Book'),
        ('MO', 'Movie'),
        ('AL', 'Musical Album'),
        ('TV', 'TV Show'),
        ('GA', 'Game'),
    )
    name = models.CharField(max_length=80)
    ent_type = models.CharField(max_length=30, default='BO', choices=ENTERTAINMENT_TYPES, verbose_name='type')
    completion_date = models.DateField(help_text='The date of completion.')
    comments = models.TextField(max_length=320, blank=True, null=True, verbose_name='additional comments')
    entry_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    entry_updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='last modified')

    def __str__(self):
        return self.name
