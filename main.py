import os
import random
import time

theBoard = {
    "top-L": "", "top-M": "", "top-R": "",
    "mid-L": "", "mid-M": "", "mid-R": "",
    "low-L": "", "low-M": "", "low-R": "",
}


def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


def isWinner(board):
    if any((board["top-L"] == board["top-M"] == board["top-R"] != "",
            board["mid-L"] == board["mid-M"] == board["mid-R"] != "",
            board["low-L"] == board["low-M"] == board["low-R"] != "",
            board["top-L"] == board["mid-L"] == board["low-L"] != "",
            board["top-M"] == board["mid-M"] == board["low-M"] != "",
            board["top-R"] == board["mid-R"] == board["low-R"] != "",
            board["top-L"] == board["mid-M"] == board["low-R"] != "",
            board["top-R"] == board["mid-M"] == board["low-L"] != ""
            )):
        return True
    else:
        return False

def people2high(board):
    flag = False
    while True:
        chess_box = ["top-L", "top-M", "top-R",
                     "mid-L", "mid-M", "mid-R",
                     "low-L", "low-M", "low-R"]
        if not flag:
            printBoard(board)
            player1 = input("玩家1执X，输入是：")
            if board[player1] == "":
                board[player1] = "X"
                flag = True
                os.system('cls')
            else:
                print("这个位置有人下过了，请重新输入！")
                continue
            if isWinner(board):
                print("玩家1胜利！")
                break
            elif isDraw(board):
                print("平局！")
                break
        else:
            printBoard(board)
            for k, v in board.items():
                if v != "":
                    chess_box.remove(k)

            com = random.choice(chess_box)
            print(f"电脑的选择是{com}")
            board[com] = "O"
            flag = False
            time.sleep(1)
            os.system('cls')
            if isWinner(board):
                print("电脑胜利！")
                break
            elif isDraw(board):
                print("平局！")
                break

def people2low(board):
    flag = False
    while True:
        chess_box = ["top-L", "top-M", "top-R",
                     "mid-L", "mid-M", "mid-R",
                     "low-L", "low-M", "low-R"]
        if not flag:
            printBoard(board)
            player1 = input("玩家1执X，输入是：")
            if board[player1] == "":
                board[player1] = "X"
                flag = True
                os.system('cls')
            else:
                print("这个位置有人下过了，请重新输入！")
                continue
            if isWinner(board):
                print("玩家1胜利！")
                break
            elif isDraw(board):
                print("平局！")
                break
        else:
            printBoard(board)
            for k, v in board.items():
                if v != "":
                    chess_box.remove(k)
            com = random.choice(chess_box)
            print(f"电脑的选择是{com}")
            board[com] = "O"
            flag = False
            time.sleep(1)
            os.system('cls')
            if isWinner(board):
                print("电脑胜利！")
                break
            elif isDraw(board):
                print("平局！")
                break


def people2people(board):
    flag = False
    while True:
        if not flag:
            printBoard(board)
            player1 = input("玩家1执X，输入是：")
            if board[player1] == "":
                board[player1] = "X"
                flag = True
                os.system('cls')
            else:
                print("这个位置有人下过了，请重新输入！")
                continue
            if isWinner(board):
                print("玩家1胜利！")
                break
            elif isDraw(board):
                print("平局！")
                break
        else:
            printBoard(board)
            player2 = input("玩家2执O，输入是：")
            if board[player2] == "":
                board[player2] = "O"
                flag = False
                os.system('cls')
            else:
                print("这个位置有人下过了，请重新输入！")
                continue
            if isWinner(board):
                print("玩家2胜利！")
                break
            elif isDraw(board):
                print("平局！")
                break


def isDraw(board):
    if all(v != "" for k, v in board.items()):
        return True
    else:
        return False


if __name__ == "__main__":
    # while True:
    #     print("---------------------")
    #     print("-----1. 人人对战 -----")
    #     print("-----2. 人机对战 -----")
    #     print("-----3. 退出游戏 -----")
    #     print("---------------------")
    #     input_index = int(input("请输入你的选择:"))
    #     os.system("cls")  # win版本需要在运行设置中勾选模拟终端才会生效
    #     if input_index == 1:
    #         people2people(theBoard)
    #         continue
    #     elif input_index == 2:
    #         print("---------------------")
    #         print("-----1. 低级电脑 -----")
    #         print("-----2. 高级电脑 -----")
    #         print("-----3. 返回上级菜单 -----")
    #         print("---------------------")
    #         input_index2 = int(input("请输入你的选择:"))
    #         os.system("cls")
    #         if input_index2 == 1:
    #             people2low(theBoard)
    #         elif input_index2 == 2:
    #             pass
    #         elif input_index2 == 3:
    #             continue
    #     elif input_index == 3:
    #         break
