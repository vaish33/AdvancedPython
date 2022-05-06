
# If you were using .kv file to make multiple layouts There is no need to import Gridlayout, 
# Boxlayout, AnchorLayout, FloatLayout, StackLayout, PageLayout, Button, etc. 
# As .kv file supports all this as It has all this imported already. 
# But if doing this without .kv file you must have to import these. 

## Sample Python application demonstrating the
## Program of How to use Multiple Layouts in Single file

########################################################################

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the childrens at the desired location.
from kivy.uix.boxlayout import BoxLayout

# The GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# The PageLayout class is used to create
# a simple multi-page layout,
# in a way that allows easy flipping from
# one page to another using borders.
from kivy.uix.pagelayout import PageLayout


########################################################################

# creating the root widget used in .kv file
class MultipleLayout(PageLayout):
	pass

########################################################################

# creating the App class in which name
#.kv file is to be named PageLayout.kv
class Multiple_LayoutApp(App):
	# defining build()
	def build(self):
		# returning the instance of root class
		return MultipleLayout()

########################################################################
	
# creating object of Multiple_LayoutApp() class
MlApp = Multiple_LayoutApp()

# run the class
MlApp.run()


##########################################################################
##########################################################################
#########################################################################

# Program of How to use Multiple Layouts in Single .kv file

########################################################################

# creating page Layout
<PageLayout>:

#########################################################################
	
	# Creating Page 1
	
	# Using BoxLayout inside PageLayout
	BoxLayout:

		# creating Canvas
		canvas:
			Color:
				rgba: 216 / 255., 195 / 255., 88 / 255., 1
			Rectangle:
				pos: self.pos
				size: self.size

		# Providing orientation to the BoxLayout
		orientation: 'vertical'

		# Adding Label to Page 1
		Label:
			size_hint_y: None
			height: 1.5 * self.texture_size[1]
			text: 'page 1'

		# Creating Button
		Button:
			text: 'GFG :)'
			
			# Adding On_press function
			# i.e binding function to press / touch
			on_press: print("This Is The First Page")

#########################################################################

	# Creating Page 2

	BoxLayout:
		orientation: 'vertical'
		canvas:
			Color:
				rgba: 109 / 255., 8 / 255., 57 / 255., 1
			Rectangle:
				pos: self.pos
				size: self.size
		Label:
			text: 'page 2'

		# This Image is directly from the websource
		# By using AsyncImage you can use that
		AsyncImage:
			source: 'http://kivy.org / logos / kivy-logo-black-64.png'

##########################################################################

	# Creating Page 3

	# Using The Second Layout
	# Creating GridLayout
	GridLayout:


		canvas:
			Color:
				rgba: 37 / 255., 39 / 255., 30 / 255., 1
			Rectangle:
				pos: self.pos
				size: self.size


		# Adding grids to Page 3
		# It may be row or column
		cols: 2


		# In first Grid
		# Adding Label + Image
		Label:
			text: 'page 3'

		AsyncImage:
			source: 'http://kivy.org/slides/kivyandroid-thumb.jpg'


		# In Second Grid
		# Adding Button + Image
		Button:
			text: 'Its User:):)'
			on_press: print("Heloo User This is the Last Page")

		AsyncImage:
			source: 'http://kivy.org/slides/kivypictures-thumb.jpg'


		# In third grid
		# Adding Widget + Image
		
		Widget

		AsyncImage:
			source: 'http://kivy.org/slides/particlepanda-thumb.jpg'
