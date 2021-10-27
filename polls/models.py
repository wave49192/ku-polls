"""This is model."""
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    """Create model."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('ending date', null=True, default=timezone.now)

    def __str__(self):
        """Return questions."""
        return self.question_text

    def was_published_recently(self):
        """Return true if questions is published recently."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Return true if question is pubblished."""
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        """Return true if question are in range of voting."""
        now = timezone.now()
        return self.end_date >= now >= self.pub_date

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    """Choices texts."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        """If this function is called it should returns choices."""
        return self.choice_text

    @property
    def votes(self):
        """Return votes in that choice."""
        return Vote.objects.filter(choice=self).count()


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=0)
