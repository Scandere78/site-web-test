from django.db import models
from teams import Team

class Tournament(models.Model):
    title = models.CharField(max_length=100)
    game = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class TournamentRegistration(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.team.name} - {self.tournament.title}'
    
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    score_team1 = models.IntegerField()
    score_team2 = models.IntegerField()
    match_date = models.DateTimeField()

    def __str__(self):
        return f'{self.team1.name} vs {self.team2.name} - {self.tournament.title}'
