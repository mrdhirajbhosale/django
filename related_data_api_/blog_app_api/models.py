from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    blog_title = models.CharField(max_length=100)
    blog_content = models.CharField(max_length=256)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default="")
    comment = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
