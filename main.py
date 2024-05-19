__version__="1.0"
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton,MDRaisedButton
Window.size=(360,620)
class Login(MDScreenManager):
    pass
class Home(MDScreen):
    def change_style(self):
        if self.theme_cls.theme_style=='Dark':
            self.theme_cls.theme_style='Light'    
        elif self.theme_cls.theme_style=='Light':
            self.theme_cls.theme_style='Dark'                    
class Bein_fhd(MDScreen):
    pass
class Bein_hd(MDScreen):
    pass
class Bein_sd(MDScreen):
    pass
class SSC_sport(MDScreen):
    pass
class AD_sport(MDScreen):
    pass
class Bein_sport1_fhd_player(MDScreen):
    pass
class Bein_sport2_fhd_player(MDScreen):
    pass
class Bein_sport3_fhd_player(MDScreen):
    pass
class Bein_sport4_fhd_player(MDScreen):
    pass
class Bein_sport5_fhd_player(MDScreen):
    pass
class Bein_sport6_fhd_player(MDScreen):
    pass
class Bein_sport7_fhd_player(MDScreen):
    pass
class Bein_sport8_fhd_player(MDScreen):
    pass
class Bein_sport9_fhd_player(MDScreen):
    pass
class Bein_sport1_hd_player(MDScreen):
    pass
class Bein_sport2_hd_player(MDScreen):
    pass
class Bein_sport3_hd_player(MDScreen):
    pass
class Bein_sport4_hd_player(MDScreen):
    pass
class Bein_sport5_hd_player(MDScreen):
    pass
class Bein_sport6_hd_player(MDScreen):
    pass
class Bein_sport7_hd_player(MDScreen):
    pass
class Bein_sport8_hd_player(MDScreen):
    pass
class Bein_sport9_hd_player(MDScreen):
    pass
class Bein_sport1_sd_player(MDScreen):
    pass
class Bein_sport2_sd_player(MDScreen):
    pass
class Bein_sport3_sd_player(MDScreen):
    pass
class Bein_sport4_sd_player(MDScreen):
    pass
class Bein_sport5_sd_player(MDScreen):
    pass
class Bein_sport6_sd_player(MDScreen):
    pass
class Bein_sport7_sd_player(MDScreen):
    pass
class Bein_sport8_sd_player(MDScreen):
    pass
class Bein_sport9_sd_player(MDScreen):
    pass
class SSC_sport1_player(MDScreen):
    pass
class SSC_sport2_player(MDScreen):
    pass
class SSC_sport3_player(MDScreen):
    pass
class SSC_sport4_player(MDScreen):
    pass
class SSC_sport5_player(MDScreen):
    pass
class SSC_sport_extra1_player(MDScreen):
    pass
class SSC_sport_extra2_player(MDScreen):
    pass
class SSC_sport_extra3_player(MDScreen):
    pass
class SSC_sport_news_player(MDScreen):
    pass
class AD_sport1_sd_player(MDScreen):
    pass
class AD_sport2_sd_player(MDScreen):
    pass
class AD_sport1_hd_player(MDScreen):
    pass
class AD_sport2_hd_player(MDScreen):
    pass
class AD_sport1_4k_player(MDScreen):
    pass
class AD_sport2_4k_player(MDScreen):
    pass
class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="DeepPurple"
        self.theme_cls.primary_hue="700"
        self.theme_cls.theme_style="Light"
        kv=Builder.load_file("main.kv")
        return kv           
if __name__=='__main__':
    MyApp().run()