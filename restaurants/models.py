from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    opening_time = models.TextField()
    closing_time = models.TextField()

    def __str__(self):
        return "%s,%s" % (self.name, self.opening_time)

