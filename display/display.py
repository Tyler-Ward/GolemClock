from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

class LCDLinearScroll:
	"""
	A class which enables one to display a linear list of items.
	The list of items can be scrolled through
	"""

	def __init__(self, items, display=Adafruit_CharLCDPlate()):
		self.display = display
		self.items = items 	
		self.index = 0

	def display_next(self):
		"Displays the next item in the cycle of items"
		self.index += 1
		if self.index == len(self.items):
			self.index = 0
		self.display_current()
	
	def display_prev(self):
		"Displays the previous item in the cycle of items"
		self.index -= 1
		if self.index == -1:
			self.index = len(self.items) - 1
		self.display_current()

	def display_current(self):
		"Displays the current message"	
		self.display.clear()
		self.display.message(self.items[self.index])


	def setup_scoll_events(self):
		"""Sets up the scroll events such that left is cycles backwards
		and right cycles forwards"""

		buttons = {'left': self.display.LEFT, 'right': self.display.RIGHT}

		prev_button = None

		while True:
			if self.display.buttonPressed(buttons['left']):
				if buttons['left'] is not prev_button:
					self.display_prev()
					prev_button = buttons['left']

			if self.display.buttonPressed(buttons['right']):
				if buttons['right'] is not prev_button:
					self.display_next()
					prev_button = buttons['right']

if __name__ == '__main__':
	items = ('Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6')
	scroller = LCDLinearScroll(items)
