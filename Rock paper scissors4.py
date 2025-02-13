from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RockPaperScissorsApp(App):
    def build(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        
        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing=10)

        self.label = Label(text="choose Rock , Paper ,or Scissor", font_size=24)
        self.layout.add_widget(self.label)  

        self.rock_btn =Button(text="Rock" , font_size=20, on_press=self.play)
        self.layout.add_widget(self.rock_btn)

        self.paper_btn =Button(text="Paper" , font_size=20, on_press=self.play)
        self.layout.add_widget(self.paper_btn)

        self.scissors_btn =Button(text="Scissors" , font_size=20, on_press=self.play)
        self.layout.add_widget(self.scissors_btn)

        return self.layout
    
    def play(self, instance):
        user_choice = instance.text
        computer_choice = random.choice(self.choices)
        result = self.get_winner(user_choice, computer_choice)
        self.label.text = f"you: {user_choice} computer: {computer_choice}\n {result}"

    def get_winner(self, user, computer):
        if user == computer:
            return "It's a Tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "paper"):
            return "You Win!🎉"
        else:
            return "Computer Wins!💻"
        
if __name__ == "__main__":
    RockPaperScissorsApp().run()

        









