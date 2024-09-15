# number devided by 3 - fizz
# number devided by 5 - buzz
# number that can be devided by 3 AND 5 - Buzzfizz


empty_list = []
for i in range(1,101):
    if i % 3 == 0:
        if i % 3 == 0 and i % 5 ==0:
            empty_list.append("fizzbuzz")
            print("fizzbuzz")
        else:
            empty_list.append("fizz")
            print("fizz")
    elif i % 5 == 0:
        empty_list.append("buzz")
        print("buzz")
    else:
        print(i)
        empty_list.append(i)


# for fun lets check how many Buzz, fizz and buzzfizz we have in list two ways - inbuilt count and loop.



# list.count() method

print("\nLIST COUNT METHOD")
print(f"there is {empty_list.count("fizz")} fizz words")
print("there is",empty_list.count("buzz"),"buzz words")
print(f"there is {empty_list.count("fizzbuzz")} fizzbuzz words in {len(empty_list)} item list")


#loop method

fi = 0
bu = 0
fibu =0


for i in empty_list:
    if i == "fizz":
        fi += 1
    elif i == "buzz":
        bu += 1
    elif i == "fizzbuzz":
        fibu += 1
print("\nLOOP METHOD")
print(f"there is {fi} fizz words")
print(f"there is {bu} buzz words")
print(f"there is {fibu} fizzbuzz words")




