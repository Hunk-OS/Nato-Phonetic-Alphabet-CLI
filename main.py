import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {value['letter']: value['code'] for (index, value) in data.iterrows()}

# while True:

#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     except:
#         continue
#     else:
#         print(output_list)
#         break

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
