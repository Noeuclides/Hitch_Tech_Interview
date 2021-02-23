from typing import ClassVar
from django.db import models


class Team(models.Model):
    """Model definition for Team."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        """Meta definition for Team."""
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        """Unicode representation of Team."""
        return self.name

class Position(models.Model):
    """Model definition for Position."""

    position = models.CharField(max_length=6, unique=True)

    class Meta:
        """Meta definition for Position."""

        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        """Unicode representation of Position."""
        return self.position

class College(models.Model):
    """Model definition for College."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        """Meta definition for College."""

        verbose_name = 'College'
        verbose_name_plural = 'Colleges'

    def __str__(self):
        """Unicode representation of College."""
        return self.name



class Player(models.Model):
    """Model definition for Player."""

    full_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    number = models.PositiveSmallIntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    age = models.PositiveSmallIntegerField()
    height = models.CharField(max_length=50)
    weight = models.PositiveSmallIntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    salary = models.IntegerField(null=True)

    class Meta:
        """Meta definition for Player."""

        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        """Unicode representation of Player."""
        return self.full_name
