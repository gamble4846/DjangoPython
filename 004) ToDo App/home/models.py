from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    isdone = models.BooleanField(default=False)

    class Meta:
        db_table = "ToDoItem"