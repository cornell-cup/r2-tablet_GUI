'''
TabbedPanel
============

Test of the widget TabbedPanel.
'''

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.uix.image import Image

Builder.load_string("""

<Test>:
    size_hint: 1, 1
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'General Info' 
        Label:
            text: 'This is Cornell Cup'
            
    TabbedPanelItem:
        text: 'Visual Img'
        BoxLayout:
            Label:
                text: 'Second tab content area'
                
    TabbedPanelItem:
        text: 'Streaming'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))
                
    TabbedPanelItem:
        text: 'Sign up'
        BoxLayout:
            Label:
                text: 'Second tab content area'
            Button:
                text: 'Button that does nothing'
    

""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()



# def : constantly access the folder and check for updates for every information

if __name__ == '__main__':
    TabbedPanelApp().run()