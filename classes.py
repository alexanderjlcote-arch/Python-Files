class Point():
    def __init__(self, input1, input2, input3,):
        self.me = input1
        self.you = input2
        self.he = input3

Gabe = Point("you", "me", "also you")


test = input("Who is ")
if test == "me":
    print(test + " is " + Gabe.me)
elif test =="you":
    print(test + " is " + Gabe.you)
elif test =="he":
    print(test + " is " + Gabe.he)