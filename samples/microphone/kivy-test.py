from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder

from kivy.core.window import Window
from kivy.modules import inspector    #右ctrl+E 即可啟動 debug inspector
from kivy.modules import monitor      #添加一個指示 FPS 的紅色頂欄和一個指示輸入活動的小圖
# module kivy.modules.touchring    #在每次觸摸周圍畫一個圓圈, 設定~/.kivy/config.ini模組自動起用
from kivy.modules import showborder   #顯示小部件widget的邊框 無效!!!
showborder.start(None, None)  #顯示小部件widget的邊框

# Console 無法啟動
# from kivy.modules.console import Console, ConsoleAddon, ConsoleLabel, ConsoleAddonFps
# Console.register_addon(ConsoleAddonFps)
# Console.register_addon(ConsoleAddonAbout)


Builder.load_string('''
<GridLayout>
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            # source: '../examples/widgets/sequenced_images/data/images/button_white.png'
            source: 'C:/Python39/share/kivy-examples/widgets/sequenced_images/data/images/button_white.png'
            pos: self.pos
            size: self.size

<RootWidget>
    GridLayout:
        size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1
        Label:
            text: "I don't suffer from insanity, I enjoy every minute of it"
            text_size: self.width-20, self.height-20
            valign: 'top'
        Label:
            text: "When I was born I was so surprised; I didn't speak for a year and a half."
            text_size: self.width-20, self.height-20
            valign: 'middle'
            halign: 'center'
        Label:
            text: "A consultant is someone who takes a subject you understand and makes it sound confusing"
            text_size: self.width-20, self.height-20
            valign: 'bottom'
            halign: 'justify'
''')

class RootWidget(FloatLayout):
    pass



class MainApp(App):

    def build(self):
        # root = Button(text='My first button')
        root =  RootWidget()
        inspector.create_inspector(Window, root)    #右ctrl+E 即可啟動 debug inspector
        monitor.start(Window, root)     #添加一個指示 FPS 的紅色頂欄和一個指示輸入活動的小圖
        # Console.activated = True  #無法啟動
        return root

if __name__ == '__main__':
    MainApp().run()

