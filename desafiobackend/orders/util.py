import random
import string

from .models import Order

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	the_id = "".join(random.choice() for x in range(size))
	try:
		order = Order.objects.get(order_id=the_id)
	except Order.DoesNotExist:
		return the_id
