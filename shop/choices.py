from django.db import models

class ColorChoices(models.TextChoices):
    RED = 'red', 'Red'
    YELLOW = 'yellow', 'Yellow'
    BLUE = 'blue', 'Blue'
    GREEN = 'green', 'Green'


class MaterialChoices(models.TextChoices):
    SILK = 'silk', 'Silk'
    POLYESTER = 'polyester', 'Polyester'
    LINEN = 'linen', 'Linen'
    WOOL = 'wool', 'Wool'