from django.db import models

# Create your models here.


class member(models.Model):

    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    FIFTH_OR_HIGHER = 'fifth+'
    GRAD = 'grad'
    FACULTY = 'faculty'
    STAFF = 'staff'
    CLASSIFICATION_CHOICES = (
        (FIRST, 'First Year'),
        (SECOND, 'Second Year'),
        (THIRD, 'Third Year'),
        (FOURTH, 'Fourth Year'),
        (FIFTH_OR_HIGHER, 'Fifth Year or higher'),
        (GRAD, 'Graduate Student'),
        (FACULTY, 'Faculty'),
        (STAFF, 'Staff'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    preferred_name = models.CharField(max_length=30)
    major = models.CharField(max_length=30, null=True)
    classification = models.CharField(
        max_length=10,
        choices=CLASSIFICATION_CHOICES,
        default=FIRST)
    email = models.EmailField(max_length=254)