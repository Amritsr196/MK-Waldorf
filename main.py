from kivy.animation import Animation
from kivy.app import App
from kivy.clock import mainthread, Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.lang import Builder
from kivy.properties import NumericProperty, BooleanProperty, BoundedNumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager, RiseInTransition
from kivy.uix.video import Video
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivmob import KivMob, TestIds
from plyer import gps, vibrator
from random import randint
import math
import pickle

class Manager(ScreenManager):
    pass


class Menu(Screen):
    pass

class SelectionScreen(Screen):  
    try:
        count = pickle.load(open("wins.dat", "rb"))
    except:
        count = 2
        pickle.dump(count, open("wins.dat", "wb"))

    d2 = False
    d3 = False
    d4 = False
    d5 = False

    if count > 2:
        d2 = True
    if count > 3:
        d3 = True
    if count > 4:
        d4 = True
    if count > 5:
        d5 = True

    day2 = BooleanProperty(d2)
    day3 = BooleanProperty(d3)
    day4 = BooleanProperty(d4)
    day5 = BooleanProperty(d5)

    def Win(self, *args):
        self.count = self.count + 1
        pickle.dump(self.count, open("wins.dat", "wb"))
        print("JOE WON")
        print(self.count)


class Game(Screen):
    # class variables
    has_remembered_initial_pos = False
    my_lat = 0
    my_lon = 0
    initial_lat = 0
    initial_lon = 0
    window_value_x = Window.width / 2
    window_value_y = Window.height / 2
    visible = False
    opac = BooleanProperty(False)
    x_value = 0
    y_value = 0
    gps_x = BoundedNumericProperty(0, min=-window_value_x, max=window_value_x)
    gps_y = BoundedNumericProperty(0, min=-window_value_y, max=window_value_y)
    rand_x = randint(0, 1)
    rand_y = randint(0, 1)
    enem_x = randint(100, 550)
    neg_enem_x = -int(enem_x)
    enem_y = randint(100, 550)
    neg_enem_y = -int(enem_y)
    if rand_x == 1:
        choose_x = enem_x
    else:
        choose_x = neg_enem_x
    if rand_y == 1:
        choose_y = enem_y
    else:
        choose_y = neg_enem_y
    print("Coords:", choose_x, choose_y)
    steiner_x = NumericProperty(choose_x)
    steiner_y = NumericProperty(choose_y)
    time_since_start = 0
    timing = NumericProperty(0)
    day = 1
    difficulty = NumericProperty(300)
    t = 0
    delta_x_less = 0
    delta_x_more = 0
    delta_y_less = 0
    delta_y_more = 0
    sound1 = randint(0, 900)
    sound2 = randint(0, 900)
    sound3 = randint(0, 900)
    sound4 = randint(0, 900)
    sound5 = randint(0, 900)
    sound6 = randint(0, 900)
    sound7 = randint(0, 900)
    sound8 = randint(0, 900)
    sound9 = randint(0, 900)
    sound10 = randint(0, 900)
    sound11 = randint(0, 900)
    sound12 = randint(0, 900)
    sound13 = randint(0, 900)
    sound14 = randint(0, 900)
    sound15 = randint(0, 900)
    ran = randint(1, 3)
    is_enabled = BooleanProperty(True)

    def on_enter(self, *args):
        self.manager.get_screen("menu").ids.menu_video.state = "pause"
        if self.has_remembered_initial_pos == False:
            if platform == 'android':
                from android.permissions import request_permissions, Permission

                def callback(permissions, results):
                    if all([res for res in results]):
                        print("callback. All permissions granted.")
                    else:
                        print("callback. Some permissions refused.")

            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        pass


    def Start_game(self, *args):
        self.opac = True
        self.is_enabled = False

        if self.has_remembered_initial_pos == False:
            self.event = Clock.schedule_interval(self.update, 5)
            self.event1 = Clock.schedule_interval(self.timer, 1)
            gps_blinker = self.manager.get_screen("game").ids.blinker
            gps_blinker.blink()

        if self.day == 2:
            self.difficulty = 350

        if platform == 'android':
            from android.permissions import request_permissions, Permission

            def callback(permissions, results):
                if all([res for res in results]):
                    print("callback. All permissions granted.")
                else:
                    print("callback. Some permissions refused.")

            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)

            # Remember these permissions as they will be needed in the buildozer.spec file:
        try:
            gps.configure(on_location=self._on_location,
                          on_status=self.on_status)
            gps.start(minTime=1000, minDistance=0)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

    def stop(self):
        gps.stop()
        Clock.unschedule(self.event1)
        Clock.unschedule(self.event)

        self.has_remembered_initial_pos = False
        self.my_lat = 0
        self.my_lon = 0
        self.initial_lat = 0
        self.initial_lon = 0
        self.window_value_x = int(Window.width / 2)
        self.window_value_y = int(Window.height / 2)
        self.visible = False
        self.opac = BooleanProperty(False)
        self.x_value = 0
        self.y_value = 0
        self.gps_x = 0
        self.gps_y = 0
        self.rand_x = randint(0, 1)
        self.rand_y = randint(0, 1)
        self.enem_x = randint(100, 500)
        self.neg_enem_x = -int(self.enem_x)
        self.enem_y = randint(100, 550)
        self.neg_enem_y = -int(self.enem_y)
        if self.rand_x == 1:
            self.choose_x = self.enem_x
        else:
            self.choose_x = self.neg_enem_x
        if self.rand_y == 1:
            self.choose_y = self.enem_y
        else:
            self.choose_y = self.neg_enem_y
        self.steiner_x = self.choose_x
        self.steiner_y = self.choose_y
        self.time_since_start = 0
        self.timing = 0
        self.day = 1
        self.difficulty = 300
        self.t = 0
        self.delta_x_less = 0
        self.delta_x_more = 0
        self.delta_y_less = 0
        self.delta_y_more = 0
        self.sound1 = randint(0, 900)
        self.sound2 = randint(0, 900)
        self.sound3 = randint(0, 900)
        self.sound4 = randint(0, 900)
        self.sound5 = randint(0, 900)
        self.sound6 = randint(0, 900)
        self.sound7 = randint(0, 900)
        self.sound8 = randint(0, 900)
        self.sound9 = randint(0, 900)
        self.sound10 = randint(0, 900)
        self.sound11 = randint(0, 900)
        self.sound12 = randint(0, 900)
        self.sound13 = randint(0, 900)
        self.sound14 = randint(0, 900)
        self.sound15 = randint(0, 900)
        self.ran = randint(1, 3)

    @mainthread
    def _on_location(self, *args, **kwargs):
        self.gps_location = '\n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])
        self.my_lat = kwargs['lat']
        self.my_lon = kwargs['lon']

        if self.has_remembered_initial_pos == False:
            self.initial_lat = self.my_lat
            self.initial_lon = self.my_lon
            self.has_remembered_initial_pos = True
            print("REMBERED POS")

        self.pos_updater()

        return self.my_lat, self.my_lon, self.initial_lat, self.initial_lon, self.has_remembered_initial_pos

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def pos_updater(self):
        print("First pos:", self.initial_lat, self.initial_lon, " Current pos:", self.my_lat, self.my_lon)
        delta_lat = self.my_lat - self.initial_lat
        delta_lon = self.my_lon - self.initial_lon

        # Converter

        scaler = 1
        self.y_value = scaler * delta_lat * 111320.0
        self.x_value = scaler * delta_lon * 40075000.0 * math.cos(self.my_lat)/360.0
        print("Delta:", self.y_value, self.x_value)

        self.gps_y = int(self.y_value)
        self.gps_x = int(self.x_value)

    def update(self, dt):
        self.gps_y = int(self.y_value)
        self.gps_x = int(self.x_value)
        print("*************", self.gps_x, self.gps_y, "************")
        if self.has_remembered_initial_pos == True:
            temp_x_value = self.x_value + self.window_value_x
            temp_y_value = self.y_value + self.window_value_y
            temp_steiner_x = self.steiner_x + self.window_value_x
            temp_steiner_y = self.steiner_y + self.window_value_y

            if temp_steiner_x < temp_x_value:
                self.delta_x_less = temp_x_value - temp_steiner_x
                diff_x_less = temp_steiner_x + self.delta_x_less / 9
                self.steiner_x = int(diff_x_less) - self.window_value_x
            if temp_steiner_x > temp_x_value:
                self.delta_x_more = temp_steiner_x - temp_x_value
                diff_x_more = temp_steiner_x - self.delta_x_more / 9
                self.steiner_x = int(diff_x_more) - self.window_value_x
            if temp_steiner_y < temp_y_value:
                self.delta_y_less = temp_y_value - temp_steiner_y
                diff_y_less = temp_steiner_y + self.delta_y_less / 9
                self.steiner_y = int(diff_y_less) - self.window_value_y
            if temp_steiner_y > temp_y_value:
                self.delta_y_more = temp_steiner_y - temp_y_value
                diff_y_more = temp_steiner_y - self.delta_y_more / 9
                self.steiner_y = int(diff_y_more) - self.window_value_y
            print("Updated Steiner", self.steiner_x, self.steiner_y)

            if self.delta_x_less < 50:
                if self.delta_y_less < 50:
                    if self.delta_x_more < 50:
                        print("oh shit")
                        if self.delta_y_more < 50:
                            self.manager.transition = RiseInTransition()
                            self.manager.current = 'jumpscarescreen'
                            self.stop()
                            vibrator.vibrate(time=1)

    def timer(self, dt):
        self.time_since_start += 1
        self.timing = self.time_since_start
        print(self.timing)

        if self.time_since_start == 60:
            self.opac = False
        if self.time_since_start > 300:
            self.manager.current = 'winningscreen'
            self.stop()
            print("JOE 3")
        if self.time_since_start == self.sound1:
            Video(source='come_closer.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound2:
            Video(source='educate.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound3:
            Video(source='ich_habe.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound4:
            Video(source='laugh.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound5:
            Video(source='no_need_to_be_scared.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound6:
            Video(source='bush_rustling.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound7:
            Video(source='fast_paced_footsteps.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound8:
            Video(source='geiger.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound9:
            Video(source='knocking.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound10:
            Video(source='REPULSIVE-Cry.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound11:
            Video(source='sirenhead.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound12:
            Video(source='slow_paced_footsteps.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound13:
            Video(source='ich_habe.mp4', play=True, opacity=0)
        if self.time_since_start == self.sound14:
            Video(source='ich_habe.mp4', play=True, opacity=0)


class Cameraview(Screen):  # CAMERA and FLASHLIGHT for android permissions builder.spec
    window_value_x = Window.width / 2
    window_value_y = Window.height / 2
    visible = False
    opacit = BooleanProperty(False)
    is_enabled = BooleanProperty(True)
    the_time = NumericProperty(0)
    random_sound = int(randint(0,9))

    def __init__(self, **kwargs):
        super(Cameraview, self).__init__(**kwargs)
        self._request_android_permissions()

    @staticmethod
    def is_android():
        return platform == 'android'

    def _request_android_permissions(self):
        if not self.is_android():
            return
        from android.permissions import request_permission, Permission
        request_permission(Permission.CAMERA)

    def capture(self):
        #sound = SoundLoader.load('soft_jumpscare.ogg')
        #sound.play()
        Video(source='soft_jumpscare.mp4', play=True, opacity=0)
        vibrator.vibrate(time=0.1)
        if self.random_sound == 0:
            Video(source='sun.mp4', play=True, opacity=0)
        if self.random_sound == 1:
            Video(source='mercury.mp4', play=True, opacity=0)
        if self.random_sound == 2:
            Video(source='venus.mp4', play=True, opacity=0)
        if self.random_sound == 3:
            Video(source='earth.mp4', play=True, opacity=0)
        if self.random_sound == 4:
            Video(source='mars.mp4', play=True, opacity=0)
        if self.random_sound == 5:
            Video(source='jupiter.mp4', play=True, opacity=0)
        if self.random_sound == 6:
            Video(source='saturn.mp4', play=True, opacity=0)
        if self.random_sound == 7:
            Video(source='uranus.mp4', play=True, opacity=0)
        if self.random_sound == 8:
            Video(source='neptune.mp4', play=True, opacity=0)
        if self.random_sound == 9:
            Video(source='pluto.mp4', play=True, opacity=0)
        print("Captured")
        self.random_sound = int(randint(1,10))

    def disable_timer(self):
        self.is_enabled = False
        self.manager.get_screen("game").opac = True
        self.event2 = Clock.schedule_interval(self.cooldown, 1)

    def cooldown(self, dt):
        self.the_time += 1
        if self.the_time == 60:
            self.is_enabled = True
            self.manager.get_screen("game").opac = False
            Clock.unschedule(self.event2)
            self.the_time = 0


    def stalker(self):
        self.opacit = True

    def invisible(self):
        self.opacit = False

class MainWidget(Widget):
    V_NB_LINES = 11
    V_LINES_SPACING = .083
    vertical_lines = []

    H_NB_LINES = 12
    H_LINES_SPACING = .083
    horizontal_lines = []

    line = None
    line_y = None

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()

    def on_size(self, *args):
        self.update_vertical_lines()

    def init_vertical_lines(self):
        with self.canvas:
            Color(0, 1, 0)
            self.line = Line(points=[self.width / 2, 0, self.width / 2, self.height], width=2)
            self.line_y = Line(points=[0, self.height / 2, self.width, self.height / 2], width=2)

            Color(1, 1, 1)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())
                self.horizontal_lines.append(Line())

    def update_vertical_lines(self):
        center_x = int(self.width / 2)
        spacing_x = self.V_LINES_SPACING * self.width
        center_y = int(self.height / 2)
        spacing_y = self.H_LINES_SPACING * self.height

        self.line.points = [center_x, center_y * 2, center_x, self.height * 2]
        self.line_y.points = [0, center_y * 3, self.width, center_y * 3]
        offset = -int(self.V_NB_LINES / 2)

        for i in range(0, self.V_NB_LINES):
            line_x = int(center_x + offset * spacing_x)
            self.vertical_lines[i].points = [line_x, self.height, line_x, self.height * 2]
            offset += 1

        for i in range(0, self.H_NB_LINES):
            line_y = int(center_y + offset * spacing_y)
            self.horizontal_lines[i].points = [0, line_y, self.width, line_y]
            offset += 1


class GpsBlinker(Widget):
    def blink(self):
        anim = Animation(opacity=0, blink_size=50)
        anim.bind(on_complete=self.reset)
        anim.start(self)

    def reset(self, *args):
        self.opacity = 1
        self.blink_size = self.default_blink_size
        self.blink()


class EnemyBlinker(FloatLayout):
    pass

class WinningScreen(Screen):
    active = BooleanProperty(False)
    event = randint(0,19)
    fun = randint(1,1000000)

    def on_enter(self, *args):
        self.active = True

    def on_leave(self, *args):
        self.active = False
        if self.event == 9:
            Video(source='project.mp4', play=True, opacity=0)
        if self.event == 19:
            Video(source='steiner_log.mp4', play=True, opacity=0)
        if self.fun == 196:
            if self.event == 0:
                Video(source='gold.mp4', play=True, opacity=0)

class Credits(Screen):
    pass

class JumpscareScreen(Screen):
    active = BooleanProperty(False)
    event = randint(0, 9)

    def on_enter(self, *args):
        self.active = True

    def on_leave(self, *args):
        self.active = False
        if self.event == 9:
            Video(source='message.mp4', play=True, opacity=0)

class InterstitialAdScreen(Screen):
    INTERSTITIAL_VIDEO = '**********************************'

    ads = KivMob(INTERSTITIAL_VIDEO)
    ads.new_interstitial(INTERSTITIAL_VIDEO)
    tm = 0

    def on_pre_enter(self, *args):
        self.ads.request_interstitial()
        self.show()

    def on_pre_leave(self, *args):
        self.ads.request_interstitial()

    def on_resume(self):
        self.ads.request_interstitial()

    def show(self):
        self.event4 = Clock.schedule_interval(self.updating, 1)
        self.ads.show_interstitial()
        print("interstitial ad")

    def updating(self, dt):
        self.tm += 1
        print(self.tm)
        if self.tm > 4:
            self.manager.current = 'menu'
            Clock.unschedule(self.event4)
            print("done")

    def on_leave(self, *args):
        self.manager.get_screen("menu").ids.menu_video.state = "play"





kv = Builder.load_string("""  #:import FadeTransition kivy.uix.screenmanager.FadeTransition

Manager:
    transition: FadeTransition()
    Menu:
        name: 'menu'
    SelectionScreen:
        name:'selectionscreen'
    Game:
        name:'game'
        id: game_id
    Cameraview:
        name:'cameraview'
        id: cameraview_id
    WinningScreen:
        name: 'winningscreen'
    JumpscareScreen:
        name: 'jumpscarescreen'
    InterstitialAdScreen:
        name: 'interstitial'
    Credits:
        name: 'credits'


<GpsBlinker>
    default_blink_size: 25
    blink_size: 25

    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        RoundedRectangle:
            radius:[root.blink_size/2.0, ]
            size: [root.blink_size, root.blink_size]
            pos: root.pos[0] + root.size[0]/2.0 - root.blink_size/2.0, root.pos[1] + root.size[1]/2.0 - root.blink_size/2.0
        Color:
            rgb: 1, 0, 0
        RoundedRectangle:
            radius: [root.default_blink_size/2.0, ]
            size: [root.default_blink_size, root.default_blink_size]
            pos: [root.pos[0] + root.size[0]/2.0 - root.default_blink_size/2.0, root.pos[1] + root.size[1]/2.0 -root.default_blink_size/2.0 ]

<EnemyBlinker>
    default_blink_size: 50
    blink_size: 75

    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        RoundedRectangle:
            radius:[root.blink_size/2.0, ]
            size: [root.blink_size, root.blink_size]
            pos: root.pos[0] + root.size[0]/2.0 - root.blink_size/2.0, root.pos[1] + root.size[1]/2.0 - root.blink_size/2.0
        Color:
            rgba: 1, 0, 0, 0.5
        RoundedRectangle:
            radius: [root.default_blink_size/2.0, ]
            size: [root.default_blink_size, root.default_blink_size]
            pos: [root.pos[0] + root.size[0]/2.0 - root.default_blink_size/2.0, root.pos[1] + root.size[1]/2.0 -root.default_blink_size/2.0 ]




<Menu>
#    Video:
#        source: "TV_Static.mp4"
#        state: "play"
#        allow_stretch: True
#        keep_ratio: False
#        options: {'eos': 'loop'}
    Video:
        id: menu_video
        source: "Menuscreen.mp4"
        state: "play"
        allow_stretch: True
        options: {'eos': 'loop'}
    Image:
        source: "Title.png"
        size: self.texture_size
        pos: (0, 200)
        allow_stretch: True
    BoxLayout:
        orientation:'vertical'
        padding:'80dp', '20dp'
        spacing:'150dp'
        Widget:
        BoxLayout:
            orientation:'vertical'
            padding:'10dp'
            spacing:'25dp'
            Button:
                text:'Start'
                on_release:
                    app.root.current = "selectionscreen"
                    root.manager.transition.direction = "up"
            Button:
                text:'Exit'
                on_release:
                    app.stop()

<SelectionScreen>
    id: selectionscreen
    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'The_unenlightened_masses2.png' 
            size: self.texture_size
            allow_stretch: True
            keep_ratio: False
        Image:
            source: 'The_unenlightened_masses3.png'
            size: self.texture_size
            #allow_stretch: True
            #keep_ratio: False
        Button:
            text: 'Start'
            size_hint_y: None
            height: '196'
            on_release:
                app.root.current = "game"
        BoxLayout:
            size_hint_y: None
            height: '48dp'
            Button:
                text: 'Return'
                on_release:
                    app.root.current = "menu"
            Button:
                text: 'Credits'
                on_release:
                    app.root.current = "credits"

<Game>
    BoxLayout:
        orientation: 'vertical'
        FloatLayout:
            size_hint: 1, 3
            MainWidget:
                id: mainwidget
                pos_hint: {"center_y": 0.5}
            GpsBlinker:
                id: blinker
                pos: [root.gps_x, root.gps_y + root.height/2]
                on_pos: print("blinker pos ", self.pos)
            EnemyBlinker:
                opacity: 1 if root.opac else 0
                id: enemyblinker
                pos: (root.steiner_x, root.steiner_y + root.height/2)
                #pos: (-200,  0 + root.height/2) if root.opac else (-root.width, root.height)
        Button:
            text: "Camera"
            on_release:
                app.root.current = "cameraview"
        Label:
            id: time_id
            #size_hint: 1, 0.5
            text: str(root.difficulty - root.timing) + " Seconds To Survive"
        Button:
            #size_hint: 1, 0.5
            text: "GPS ON"
            disabled: not root.is_enabled
            on_press:
                root.Start_game()             



<Cameraview>
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            Camera:
                id: camera
                resolution: (640, 480)
                play: True
                allow_stretch: True
                canvas.before:
                    PushMatrix
                    Rotate:
                        angle: -90
                        origin: self.center
                canvas.after:
                    PopMatrix        
            Button:
                text: "Back To Main"
                pos_hint: {"center_x": .5}
                size_hint: .4, None
                height: '48dp'         
                on_release:
                    root.invisible()
                    app.root.current = "game"
                    root.manager.transition.direction = "up"
            Button:
                id: button
                text: str(60 - root.the_time) + " Seconds Cooldown" if not root.is_enabled else "Analyse"
                size_hint_y: None
                height: '48dp'
                disabled: not root.is_enabled
                on_press:
                    root.capture()
                    root.stalker()
                    root.disable_timer()
        Label:
            halign: 'left'
            valign: 'top'
            pos_hint: {"center_x": .1, "center_y": .9}
            color: 1,0,0,1
            text: "REC"

<MainWidget>
   
<WinningScreen>
    BoxLayout:
        orientation: 'vertical'
        Video:
            source: "Winning.mp4"
            state: "play" if root.active else "pause"
        Button:
            text: 'Return'
            size_hint_y: None
            height: '96dp'
            on_release:
                app.root.current = 'interstitial'
                app.win.Win()

<JumpscareScreen>
    BoxLayout:
        orientation: 'vertical'
        Video:
            source: "Jumpscare.mp4"
            state: "play" if root.active else "pause"
            #opacity: 1
        Button:
            text: 'Return'
            size_hint_y: None
            height: '96dp'
            on_release:
                app.root.transition = FadeTransition()
                app.root.current = "interstitial"

<InterstitialAdScreen>

<Credits>
    BoxLayout:
        orientation: 'vertical'
        FloatLayout:
            Label:
                halign: 'left'
                valign: 'top'
                pos_hint: {"center_x": .1, "center_y": .9}
                color: 1,0,0,1
                text: "CREDITS"
            Label:
                text: "Produced by Randhawa, Amritjit Singh"
                pos: (0, 200)
            Label:
                text: "Voice acting by Matsunaga, Hirosato"
                pos: (0, 100)
            Label:
                text: "Special thanks to REPULSIVE for the music"
                halign: 'left'
        Button:
            text: 'Return'
            size_hint_y: None
            height: '96dp'
            on_release:
                app.root.current = "selectionscreen"
        
        
""")




class MKWaldorf(App):
    start_game = Game()
    visible = Game.is_enabled
    win = SelectionScreen()



    def build(self):
        self.icon = "icon.png"
        return kv



if __name__ == '__main__':
    MKWaldorf().run()
