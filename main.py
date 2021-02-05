from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("demo.kv")

class DemoApp(App):
    def build(self):
        return presentation()

if __name__ == "__main__":
    DemoApp().run()