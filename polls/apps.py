"""Apps."""
from django.apps import AppConfig


class PollsConfig(AppConfig):
    """For polls config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
