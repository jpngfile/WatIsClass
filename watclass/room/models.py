from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Room(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    lectures = models.IntegerField("number of lectures", default=0)

    @classmethod
    def create(cls, name, lectures, code):
        room = cls(name=name, lectures=lectures, code=code)
        return room

class Lecture(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    id_num = models.SmallIntegerField()
    numVotes = models.SmallIntegerField(default=0)

class Stack(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    id_num = models.SmallIntegerField(default=0)
    size = models.SmallIntegerField(default=0)
    numVotes = models.SmallIntegerField(default=0)

class Picture(models.Model):
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)
    numVotes = models.SmallIntegerField(default=0)
    image = models.ImageField()
