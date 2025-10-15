from django.db import models
from django.contrib.auth.models import User
from feed.models import UserProfile


class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='challenge_images/', blank=True, null=True)
    reward_points = models.PositiveIntegerField(default=50)  

    def __str__(self):
        return self.title


class Submission(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    before_image = models.ImageField(upload_to='submissions/before/')
    after_image = models.ImageField(upload_to='submissions/after/')
    scale_image = models.ImageField(upload_to='submissions/scale/')
    location = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title} ({self.status})"
    def save(self, *args, **kwargs):
        # Only add points if status changes to APPROVED
        if self.pk:
            old = Submission.objects.get(pk=self.pk)
            if old.status != 'APPROVED' and self.status == 'APPROVED':
                profile = UserProfile.objects.get(user=self.user)
                profile.eco_points += self.challenge.reward_points
                profile.update_rank()
                profile.save()
        super().save(*args, **kwargs)



