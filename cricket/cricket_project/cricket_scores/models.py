# cricket_scores/models.py

from djongo import models

class Match(models.Model):
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    score_a = models.IntegerField()
    score_b = models.IntegerField()
    date = models.DateField()

    class Meta:
        app_label = 'cricket_scores'
