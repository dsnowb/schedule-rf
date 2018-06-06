__version__ = '0.1'
#class ScheduleRFApp(App):
#
#    def build(self):
#        # return ScheduleRF()
#        btn = Button(text='Disable WiFi')
#        # btn.bind(on_press=disable_wifi)
#        return btn

from jnius import autoclass
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label


def disable_wifi(instance):
    WiFiManager = autoclass('android.net.wifi.WifiManager')
    wManager = WiFiManager()
    wManager.setWifiEnabled(False)


class ScheduleRF(Widget):
    pass


class ScheduleRFApp(App):
    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    ScheduleRFApp().run()
