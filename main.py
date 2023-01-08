from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

class Main_Screen(Screen):
    pass
class Screen_2(Screen):
    pass
class Screen_3(Screen):
    pass
class sm(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        return

if __name__ == "__main__":
    MainApp().run()