import random

class Game:
    def __init__(self):
        self.board = ["","","","","","","","",""]

    def make_board(self):
        new_list = []
        for i in self.board:
            if i == "":
                new_list.append("-")
            elif "x" in i:
                new_list.append("x")

            else:
                new_list.append("o")
        for i in range(1,4):
            print(new_list[(3*i)-3]+new_list[(3*i)-2]+new_list[(3*i)-1])
            
    @staticmethod
    def print_board_nums():
        print("You select which number you want as a position for your input ur choice")
        i = 3
        for x in range(3):
            print(" "+str(i*x)," " + str((i*x)+1)," "+str((i*x)+2))
        for i in range(5):
            print("                                 ")
            
    def get_computer_move(self):
        f = True
        while f == True:
            p = random.randint(0,8)
            if self.board[p] == "":
                print("good")
                f = False
        self.board[p] = "o"
            
    def get_winner(self):
        char = ""
        count = 0
        if self.board == ["","","","","","","","",""]:
            print("suis")
            return True
        elif self.board[0] == self.board[4] == self.board[8] and self.board[4] != "":
            count += 1
            char = self.board[4]
        elif self.board[2] == self.board[4] == self.board[6] and self.board[4] != "":
            count += 1
            char = self.board[4]
        else:
            for i in range(3):
                if self.board[i] == self.board[i+(1*3)] == self.board[i+(2*3)] and self.board[i] != "":
                                               char = self.board[i]
                                               count += 1
                elif self.board[3*i] == self.board[(3*i)+1] == self.board[(3*i)+2] and self.board[3*i] != "":
                    char = self.board[3*i]
                    count += 1
        if count != 0:
            return False


    def make_move(self):
        dec = True
        while dec == True:
            print("where do you want to play x ")
            ans = int(input())
            if self.board[ans] == "":
                print("nice")
                dec = False

        self.board[ans] = "x"



        
