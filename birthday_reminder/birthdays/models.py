from django.conf import settings
from django.db import models


class Birthday(models.Model):
    # JANUARY = "January"
    # FEBRUARY = "February"
    # MARCH = "March"
    # APRIL = "April"
    # MAY = "May"
    # JUNE = "June"
    # JULY = "July"
    # AUGUST = "August"
    # SEPTEMBER = "September"
    # OCTOBER = "October"
    # NOVEMBER = "November"
    # DECEMBER = "December"

    MONTH_CHOICES = (
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"),
        ("May", "May"),
        ("June", "June"),
        ("July", "July"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November", "November"),
        ("December", "December")
    )

    DAY_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
        (21, 21),
        (22, 22),
        (23, 23),
        (24, 24),
        (25, 25),
        (26, 26),
        (27, 27),
        (28, 28),
        (29, 29),
        (30, 30),
        (31, 31)
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)

    month = models.CharField(
        max_length=100,
        choices=MONTH_CHOICES,
        default="January"
    )
    day = models.IntegerField(
        choices=DAY_CHOICES,
        default=1
    )

    def __str__(self):
        return self.name
