from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    ask_question = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.ask_question

    def get_responses(self):

        #print(self.responses.filter(parent=None))
        return self.responses.filter(parent=None)

class Answer(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE, related_name='responses')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    post_answer = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User,related_name='blog_post')


    def __str__(self):
        return self.post_answer
    def total_likes(self):
        return self.likes.count()
