from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.app import App
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout





class MyLayout(BoxLayout):
    
    def rannum1(self, n):
        return random.randint(0, n)
    def rannum2(self, n):
        return random.randint(0, n)
    def rannum3(self, n):
        return random.randint(0, n)
    
    def get_score(self):
        score =self.num1 + self.num2 + self.num3
        return score
    
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.font_size = 75
        self.padding = 75
        self.spacing = 40

        self.orientation = 'horizontal'
        self.padding = 75

        self.round_counter  = 1
        
        
        self.num1 = self.rannum1(100)
        self.num2 = self.rannum2(100)
        self.num3 = self.rannum3(100)
        
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)

        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')

        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)

        self.add_widget(center_layout)
        
    
    def reset(self, instance):
        self.clear_widgets()
        self.round_counter  = 1
        
        
        self.num1 = self.rannum1(100)
        self.num2 = self.rannum2(100)
        self.num3 = self.rannum3(100)
        
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)

        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')

        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)

        self.add_widget(center_layout)
        
    
    
    def on_button_press(self, instance):
        # define what happens when the button is pressed
        print('Button pressed!')
        self.clear_widgets()
        button4 = RoundedButton(text='Increase',  font_size=50)
        self.add_widget(button4)
        button5 = RoundedButton(text='Decrease',  font_size=50)
        self.add_widget(button5)
        button4.bind(on_press=self.increase)
        button5.bind(on_press=self.decrease)
        
    def on_button_press1(self, instance):
        # define what happens when the button is pressed
        print('Button pressed!')
        self.clear_widgets()
        button6 = RoundedButton(text='Increase',  font_size=50)
        self.add_widget(button6)
        button7 = RoundedButton(text='Decrease',  font_size=50)
        self.add_widget(button7)
        button6.bind(on_press=self.increase1)
        button7.bind(on_press=self.decrease1)
        
    def on_button_press2(self, instance):
        # define what happens when the button is pressed
        print('Button pressed!')
        self.clear_widgets()
        button8 = RoundedButton(text='Increase',  font_size=50)
        self.add_widget(button8)
        button9 = RoundedButton(text='Decrease',  font_size=50)
        self.add_widget(button9)
        button8.bind(on_press=self.increase2)
        button9.bind(on_press=self.decrease2)
        

    def increase(self, instance):
        print('Increase')
        
        addition = self.rannum1(self.num1)
        self.num1 = self.num1 + addition
        
        self.clear_widgets()
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)
        self.round_counter += 1
        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')
        
        
        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)
        
        self.add_widget(center_layout)
        if self.get_score == 101:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            win_label = Label(text='You Win')
            center_layout1.add_widget(win_label)
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
        
        if self.round_counter == 4:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
            
        


        
        
    def decrease(self, isntance):
        print('Decrease')
        subtraction = self.rannum1(self.num1)
        self.num1 = self.num1 - subtraction
        self.clear_widgets()
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)
        self.round_counter += 1
        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')

        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)

        self.add_widget(center_layout)
        if self.get_score == 101:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            win_label = Label(text='You Win')
            center_layout1.add_widget(win_label)
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
        
        if self.round_counter == 4:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
            
        
        
    def increase1(self, instance):
        print('Increase')
        addition = self.rannum1(self.num2)
        self.num2 = self.num2 + addition
        self.clear_widgets()
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)
        self.round_counter += 1
        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')

        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)

        self.add_widget(center_layout)
        if self.get_score == 101:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            win_label = Label(text='You Win')
            center_layout1.add_widget(win_label)
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
        
        if self.round_counter == 4:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
            
        
        
    def decrease1(self, isntance):
        print('Decrease')
        subtraction = self.rannum1(self.num2)
        self.num2 = self.num2 - subtraction
        self.clear_widgets()
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)

        self.round_counter += 1
        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')

        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)

        self.add_widget(center_layout)
        if self.get_score == 101:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            win_label = Label(text='You Win')
            center_layout1.add_widget(win_label)
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
        
        if self.round_counter == 4:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
            
        
        
    def increase2(self, instance):
        print('Increase')
        addition = self.rannum1(self.num3)
        self.num3 = self.num3 + addition
        self.clear_widgets()
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)

        self.round_counter += 1
        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')
        
        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)

        self.add_widget(center_layout)
        if self.get_score == 101:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            win_label = Label(text='You Win')
            center_layout1.add_widget(win_label)
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
        
        if self.round_counter == 4:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
            
        
        
    def decrease2(self, isntance):
        print('Decrease')
        subtraction = self.rannum1(self.num3)
        self.num3 = self.num3 - subtraction
        self.clear_widgets()
        buttons_layout = BoxLayout(spacing=40)
        button1 = RoundedButton(text=str(self.num1), font_size=self.font_size, size_hint=(None, None), size=(200, 100))
        button2 = RoundedButton(text=str(self.num2), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))
        button3 = RoundedButton(text=str(self.num3), font_size=self.font_size, size_hint=(0.5, 0.2), size=(200, 100))


        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press1)
        button3.bind(on_press=self.on_button_press2)

        buttons_layout.add_widget(button1)
        buttons_layout.add_widget(button2)
        buttons_layout.add_widget(button3)

        self.round_counter += 1
        score_label = Label(text='Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
        round_couter = Label(text='Round: ' + str(self.round_counter), font_size=50, halign='center', valign='middle')

        center_layout = BoxLayout(orientation='vertical')
        center_layout.add_widget(Label())
        center_layout.add_widget(buttons_layout)
        center_layout.add_widget(score_label)
        center_layout.add_widget(round_couter)

        self.add_widget(center_layout)
        if self.get_score == 101:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            win_label = Label(text='You Win')
            center_layout1.add_widget(win_label)
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
        
        if self.round_counter == 4:
            buttons_layout.clear_widgets()
            center_layout.clear_widgets()

            center_layout1 = BoxLayout(orientation='vertical')
            score_label = Label(text='Final Score: ' + str(self.get_score()), font_size=50, halign='center', valign='middle')
            center_layout1.add_widget(score_label)

            anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
            reset_button = RoundedButton(text='Try Again', font_size=50)
            reset_button.bind(on_press=self.reset)
            anchor_layout.add_widget(reset_button)
            center_layout1.add_widget(anchor_layout)

            center_layout.add_widget(center_layout1)
            
        
        

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        with self.canvas.before:
            Color(48/255, 84/255, 150/255, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[58])
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        self.size_hint = (.5, .5)
        #self.size = (200, 100)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos




class MyApp(App):
    def build(self):
        layout = MyLayout()

        return layout
    
    


if __name__ == '__main__':
    MyApp().run()
