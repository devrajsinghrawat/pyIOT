# def match_name():
#     userName = input("Enter your name : ")
#     selected_word = fetch_flower(userName[0].upper())
#     print(selected_word)


# def fetch_flower(first_word):
#     with open('./flower.txt', 'r') as f:
#         # dict = f.readlines()
#         filtered_word = ''
#         for line in f:
#             if (line.startswith(first_word)):
#                 filtered_word = line.strip()
#                 # print(filtered_word)
#                 break

#     return filtered_word


# if __name__ == '__main__':
#     match_name()
# function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main():
    flower_d = create_flowerdict('flower.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()