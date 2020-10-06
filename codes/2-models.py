class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    config = models.JSONField()
