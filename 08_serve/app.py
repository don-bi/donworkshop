from flask import Flask
import random

def get_last_comma(str):
    #takes a sting and returns the index of the last comma (for use in parsing a csv)
    reversed_string = str[::-1]
    for index in range(len(reversed_string)):
        if reversed_string[index] == ",":
            return len(str) - index - 1
    return -1

def csv_to_dictionary():
    #takes a csv containing occupations and the % of people employed in them and converts it into a dict
    info = open("occupations.csv")
    lines = info.read().split("\n")

    occupation_to_percentage = {}
    for i in lines[1:-1]:
        last_comma = get_last_comma(i)
        occupation = i[:last_comma]
        percentage = i[last_comma + 1:]

        occupation_to_percentage[occupation] = float(percentage)

    total_line = lines[-1]
    total_line_comma = get_last_comma(total_line)
    total_percentage = float(total_line[total_line_comma + 1:])

    return occupation_to_percentage, total_percentage


def get_random_occupation():
    #finds a random occupation based on the % they appear
    occupation_to_percentage, total_percentage = csv_to_dictionary()
    random_seed = random.random() * total_percentage #0 inclusive - 99.8 exclusive

    cumulative_value = 0
    for key, value in occupation_to_percentage.items():
        cumulative_value += value

        if cumulative_value > random_seed:
            return key

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    thigns = get_random_occupation()
    return f'Brian Yang, Donald Bi, Faiyaz Rafee <br> SoftDev <br> K08 --Flask <br> 2022-10-06 <br> time spent:1hr<br> <br>{csv_to_dictionary()[0]} <br> <br> {get_random_occupation()}'

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()