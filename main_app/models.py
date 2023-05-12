from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.
SCORES = (
    ('P', 'Poor'),
    ('A', 'Average'),
    ('O', 'Outstanding')
)

class Collectible(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('collectibles_detail', kwargs={'pk': self.id})
        


class Game(models.Model):
    name = models.CharField(max_length= 250)
    genre = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    collectibles = models.ManyToManyField(Collectible)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    

class Reviews(models.Model):
    date = models.DateField('review date')
    score = models.CharField(
        max_length=1,
        choices=SCORES,
        default=SCORES[1][1]
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.get_score_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
