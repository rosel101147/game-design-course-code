from GameController import GameController

class Runner:
    def __init__(self):
        self.number_of_games_played = 0
        self.max_number_of_days_survived = 0
        self.playing = True
    
    def play(self):
        # Intro message
        print("Welcome to Escape The Island!! ")
        while(self.playing):
            newGame = GameController()
            newGame.play()
            self.save_number_of_max_days(newGame.days)
            self.number_of_games_played +=1
            self.playing = self.ask_to_play_again()

    def ask_to_play_again(self):
        while(True):
            play_again = input("Play again? (Y/N) ")
            if play_again == "Y":
                return True
            elif play_again == "N":
                return False
            else:
                print("I don't understand. Say that again please: ")

            
    def save_number_of_max_days(self, days_survived):
        if days_survived > self.max_number_of_days_survived:
            self.max_number_of_days_survived = days_survived
        print("You have survived a maximum of " + str(self.max_number_of_days_survived) + " days. ")