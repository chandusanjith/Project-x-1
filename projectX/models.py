from django.db import models

class Roles(models.Model):
  role_id = models.CharField(max_length=16, default="", null=False)
  role_name = models.CharField(max_length=100, default=" ")
  role_description = models.TextField()
  role_access = models.CharField(max_length=100, default=" ")
  updated_at = models.DateField(auto_now_add=True)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
      return self.role_id
