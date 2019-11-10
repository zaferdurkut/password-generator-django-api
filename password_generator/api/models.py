from django.db import models

class Password(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.NullBooleanField(null=True,default=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return str(self.password)

    def get_password(self):
        return self.password
