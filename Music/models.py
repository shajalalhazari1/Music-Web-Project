from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=50)
    instrument = models.CharField(max_length= 50)

    def __str__(self):
        return "{}".format(self.name)


class Album(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_star = ((1, 'Wrost'),(2,'Bad'),(3,'Not Bad'),(4,'Good'),(5,'Excellent!'))
    rating = models.IntegerField(choices=num_star)

    def __str__(self):
        return "{} by {}".format(self.name, self.singer)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    other_singer = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} form {} {}".format(self.name, self.album, self.other_singer)