from django.db import models

class Stock(models.Model):
	name = models.CharField(max_length=255)
	ticker = models.CharField(max_length=255)
	
	def __repr__(self):
		return self.name
	
class Price(models.Model):
	value = models.DecimalField(max_digits=6, decimal_places=2)
	date = models.DateTimeField(auto_now_add=True, db_index=True)
	asset = models.ForeignKey("Stock")
	class Meta:
		get_latest_by = 'date'
	
	def __repr__(self):
		return self.value
