#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
#  This program is free software: you can redistribute it and/or modify

from random import randint


class Guess:
    def __init__(self):
        self.__answer = randint(1, 100)  # 1-100 arasında rastgele sayı üretir
        self.__counter = 0  # tahmin sayısını tutar
        self.__result = False  # sonucu tutar (True/False)

    def guess(self):
        while self.__result == False:
            self.__counter += 1
            try:
                number = int(input("Guess the number: "))
            except ValueError:
                print("Please enter a number.")
            else:
                if number < self.__answer:
                    print("Please guess higher.")
                elif number > self.__answer:
                    print("Please guess lower.")
                else:
                    self.__result = True
                    print("You got it.")
                    print("It took you {} times to guess the number.".format(self.__counter))

    def play(self):
        self.guess()
        while True:
            choice = input("Do you want to play again? (y/n): ")
            if choice == "y":
                self.__answer = randint(1, 100)
                self.__counter = 0
                self.__result = False
                self.guess()
            elif choice == "n":
                print("Goodbye.")
                break
            else:
                print("Please enter a valid choice.")


if __name__ == "__main__":
    game = Guess()
    game.play()
