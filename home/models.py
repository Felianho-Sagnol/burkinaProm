from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    """This is the burkinaPromo home page"""

    max_count = 1

    class Meta:
        verbose_name = " Page Accueil"
        verbose_name_plural = "Pages Accueil"
