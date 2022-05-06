
### Python ---  Layouts in layouts (Multiple Layouts) in Kivy

    Kivy is a platform independent GUI tool in Python. As it can be run on Android, IOS, linux and Windows 
    etc. It is basically used to develop the Android application, but it does not mean 
    that it can not be used on Desktops applications.

    In kivy there are many Types of Layouts:  

    1.AnchorLayout: Widgets can be anchored to the ‘top’, ‘bottom’, ‘left’, ‘right’ or ‘center’.
    2. BoxLayout: Widgets are arranged sequentially, in either a ‘vertical’ or a ‘horizontal’ orientation.
    3. FloatLayout: Widgets are essentially unrestricted.
    4. RelativeLayout: Child widgets are positioned relative to the layout.
    5. GridLayout: Widgets are arranged in a grid defined by the rows and cols properties.
    6. PageLayout: Used to create simple multi-page layouts, in a way that allows easy flipping from one page to another using borders.
    7. ScatterLayout: Widgets are positioned similarly to a RelativeLayout, but they can be translated, rotate and scaled.
    8. StackLayout: Widgets are stacked in a lr-tb (left to right then top to bottom) or tb-lr order.

    Note:You can use as many as you can in a single file.

    Basic Approach to create multiple layouts in one file: 

    1) import kivy
    2) import kivyApp
    3) import BoxLayout
    4) import 
    4) set minimum version(optional)
    5) Extend the container class
    6) set up .kv file :
    7) create App class
    8) return container class or layout
    9) Run an instance of the class 

    