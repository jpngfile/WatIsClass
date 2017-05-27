from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    lectures = models.IntegerField("number of lectures", default=0)

    # noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
    @classmethod
    def create(cls, name, lectures, code):
        # noinspection PyPep8,PyPep8

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
