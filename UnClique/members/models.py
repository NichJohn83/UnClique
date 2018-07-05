from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.


class Member(models.Model):
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

    subscribed = models.BooleanField(null=False, default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    preferred_name = models.CharField(max_length=30)
    major = models.CharField(max_length=30, null=True)
    classification = models.CharField(
        max_length=10,
        choices=CLASSIFICATION_CHOICES,
        default=FIRST)
    email = models.EmailField(max_length=254)
    current_match_email = models.EmailField(max_length=254, null=True)
    secondary_match_email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
    instance.member.save()

