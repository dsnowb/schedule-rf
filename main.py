__version__ = '0.1'

from jnius import autoclass
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button

Context = autoclass('android.content.Context')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
activity = PythonActivity.mActivity


def disable_wifi(dt):
    wifi_service = activity.getSystemService(Context.WIFI_SERVICE)
    wifi_service.setWifiEnabled(False)


def enable_wifi():
    wifi_service = activity.getSystemService(Context.WIFI_SERVICE)
    wifi_service.setWifiEnabled(True)


def schedule_rf(instance):
    # disable_wifi()
    Clock.schedule_once(disable_wifi, 10)
    # Clock.schedule_once(enable_wifi, 6)


class ScheduleRFApp(App):
    def build(self):
        btn = Button(text='Disable Wifi')
        btn.bind(on_press=schedule_rf)
        return btn


if __name__ == '__main__':
    ScheduleRFApp().run()
