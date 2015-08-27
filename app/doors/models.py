from django.db.models import *
import gpio

class Door(Model):
	name = CharField('Naam', max_length=128)
	gpio_on = CharField('GPIO aan', max_length=8)
	gpio_off = CharField('GPIO uit', max_length=8)
	status = BooleanField('Aan/uit', default=False)

	def toggle(self):
		if self.status:
			self.close()
		else:
			self.open()
		self.status = not self.status
		self.save()

	def open(self):
		gpio.open_door(self)

	def close(self):
		gpio.close_door(self)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Deur"
		verbose_name_plural = "Deuren"
