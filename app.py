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
        RstDocument:
            text:
                '\\n'.join(("Hi there :)", "-----------",
                "This is Cornell Cup. "
                "I am R2. Nice to meet you!"))

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

    TabbedPanelItem:
        text: 'testing'
        BoxLayout:

            BoxLayout:
                size_hint_y: 0.4
                size_hint_x: .3
                orientation: 'horizontal'

                Label:
                    text: "Enter your email"
                    size_hint_x: .25
                    spacing: .2, .2

                TextInput:
                    id: txt_searh
                    text: ""
                    size_hint_x: .3
                    spacing: .2, .2

                Label:
                    id: lbl_search
                    size_hint_y:None

""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()



# def : constantly access the folder and check for updates for every information

if __name__ == '__main__':
    TabbedPanelApp().run()
