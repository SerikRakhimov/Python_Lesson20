from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=150)
  floor = models.IntegerField( )
  room_number = models.IntegerField( )

  def __str__(self):
    return f"{self.name} , floor: {self.floor}, room_num: {self.room_number}"

class Meeting(models.Model):
  title = models.CharField(max_length=150)
  date = models.DateField( )
  start_time = models.TimeField(default=datetime.now( ))
  duration = models.IntegerField(default=1)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)

  def __str__(self):
    return f"title {self.title}, date: {self.date}"
