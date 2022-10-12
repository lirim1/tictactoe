from game import Game


g = Game()



class Play(Game):
    def start_game(self):
        g.print_board_nums()
        g.make_board()
        for i in range(5):
            g.make_move()
            if g.get_winner() == False:
                g.make_board()
                print("Well done you have won the game!")
                break
            g.get_computer_move()
            if g.get_winner() == False:
                g.make_board()
                print("Unlucky you lost the game!")
                break
            g.make_board()
 
p = Play()

p.start_game()
