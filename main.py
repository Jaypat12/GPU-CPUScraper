from functions import find_graphics_card, find_cpu_card
import json

value = input("Searching for GPU or CPU?")
if(value.lower() == "cpu"):
    value2 = input("Please enter search term?")
    print(find_cpu_card(value2))
elif(value.lower() == "gpu"):
    value2 = input("Please enter search term?")
    print(find_cpu_card(value2))





