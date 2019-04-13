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
        text: "testing input"
        BoxLayout:

            BoxLayout:
                size_hint_y: 0.4
                size_hint_x: .3
                orientation: 'horizontal'

                Label:
                    text: "Enter your email"
                    size_hint_x: .25
                    size_hint_y: 1
                    spacing: .2, .2

                TextInput:
                    id: txt_searh
                    text: ""
                    size_hint_x: .5
                    size_hint_y: 0.1
                    spacing: .2, .2

                Label:
                    id: lbl_search
                    size_hint_y:None

    TabbedPanelItem:
        text: 'testing layout'
        BoxLayout:
            size_hint_x: 1
            size_hint_y: 1
            Label:
                size_hint_x: 0.3
                halign: "left"
                valign: "top"
                text: "Enter your email"
            BoxLayout:
                size_hint_x: 0.7
                size_hint_y: 1
                halign: "left"
                valign: "top"
                TextInput:
                    id: txt_searh
                    text: "email here"
                    size_hint_x: 0.3
                    size_hint_y: 0.1
                    valigh: "middle"
                    spacing: .2,.2
                Button:
                    text: "Complete"
                    size_hint_x: 0.1
                    size_hint_y: 0.2
                    color:


""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()



# def : constantly access the folder and check for updates for every information

if __name__ == '__main__':
    TabbedPanelApp().run()
