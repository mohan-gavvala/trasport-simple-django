from django.contrib import admin
from Q_and_A_app.models import Question,Answer

# Register your models here.
class Question_Admin(admin.ModelAdmin):
    list_display=['id','author','ask_question','created_at','updated_at']
admin.site.register(Question,Question_Admin)

class Answe_Admin(admin.ModelAdmin):
    list_display=['id','user','question','parent','post_answer','created_at','updated_at']
admin.site.register(Answer,Answe_Admin)
