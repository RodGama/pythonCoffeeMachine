# Write your code here
class CoffeeMachine:
    cups = 0
    water_a = 0
    milk_a = 0
    cafe_a = 0
    money_caixa = 0
    money_retirado = 0

    def __init__(self, cafe, cup, milk, money, water):
        self.cups = cup
        self.water_a = water
        self.milk_a = milk
        self.money_caixa = money
        self.cafe_a = cafe

    def how_many_supplies(self):
        return "The coffee machine has:\n {} of water\n {} of milk\n {} of coffee beans\n {} of disposable cups\n {} of money\n".format(self.water_a,self.milk_a,self.cafe_a,self.cups,self.money_caixa)

    def fill(self):
        water = int(input("Write how many ml of water do you want to add:"))
        milk = int(input("Write how many ml of milk do you want to add:"))
        cafe = int(input("Write how many grams of coffee beans do you want to add:"))
        cup = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.water_a = self.water_a + water
        self.milk_a = self.milk_a + milk
        self.cafe_a = self.cafe_a + cafe
        self.cups = self.cups + cup
        print("")

    def take(self):
        self.money_retirado = self.money_retirado + self.money_caixa
        aux = self.money_caixa
        self.money_caixa = 0
        return "I gave you ${}\n".format(aux)

    def buy(self,tipo_cafe):
        if tipo_cafe == 1:
            if min(self.water_a // 250, self.cafe_a // 16) and self.cups > 0:
                print("I have enough resources, making you a coffee!")
                self.money_caixa = self.money_caixa + 4
                self.water_a = self.water_a - 250
                self.cafe_a = self.cafe_a - 16
                self.cups = self.cups - 1
            else:
                print("Sorry, not enough water!")
        elif tipo_cafe == 2:
            if min(self.water_a // 350, self.cafe_a // 25, self.milk_a // 75) and self.cups > 0:
                print("I have enough resources, making you a coffee!")
                self.money_caixa = self.money_caixa + 7
                self.water_a = self.water_a - 350
                self.cafe_a = self.cafe_a - 20
                self.milk_a = self.milk_a - 75
                self.cups = self.cups - 1
            else:
                print("Sorry, not enough water!")
        elif tipo_cafe == 3:
            if min(self.water_a // 200, self.cafe_a // 12, self.milk_a // 100) and self.cups > 0:
                print("I have enough resources, making you a coffee!")
                self.money_caixa = self.money_caixa + 6
                self.water_a = self.water_a - 200
                self.cafe_a = self.cafe_a - 12
                self.milk_a = self.milk_a - 100
                self.cups = self.cups - 1
            else:
                print("Sorry, not enough water!")
        print("")


def menu():
    while 1 == 1:
        print("Write action (buy, fill, take, remaining, exit):")
        action = str(input()).strip().lower()
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            tipo_cafe = str(input())
            if tipo_cafe != "back":
                machine.buy(int(tipo_cafe))
        elif action == "take":
            print(machine.take())
        elif action == "fill":
            machine.fill()
        elif action == "remaining":
            print("")
            print(machine.how_many_supplies())
        elif action == "exit":
            break


cups = 9
water_a = 400
milk_a = 540
cafe_a = 120
money_caixa = 550
money_retirado = 0

machine = CoffeeMachine(cafe_a, cups, milk_a, money_caixa, water_a)
menu()
