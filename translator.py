
Hausa_dict = {
    "hello": "sannu",
    "thank you": "na gode",
    "water": "ruwa",
    "house": "gida",
    "food": "abinci",
    "come": "zo",
    "go": "je",
    "good": "mai kyau",
    "book": "littafi",
    "money": "kudi",
    "father": "uba",
    "mother": "uwa",
    "child": "yaro",
    "market": "kasuwa",
    "road": "hanya",
    "friend": "aboki",
    "sun": "rana",
    "moon": "wata",
    "star": "tauraro",
    "day": "rana"
}

yoruba_dictionary = {
    "hello": "ẹ̀ kaasan",
    "good morning": "ẹ̀ kaárọ̀",
    "thank you": "ẹ jẹ́jú",
    "please": "jọ̀wọ́",
    "yes": "bẹ́ẹ̀ni",
    "no": "rárá",
    "water": "omi",
    "sun": "òòrùn",
    "moon": "òṣùpá",
    "house": "ilé",
    "food": "oúnjẹ",
    "man": "ọkùnrin",
    "woman": "obìnrin",
    "child": "ọmọ",
    "love": "ìfẹ́",
    "friend": "ọ̀rẹ́",
    "come": "wá",
    "go": "lọ",
    "book": "ìwé",
    "money": "owó"
}

language_map = {
    "hausa": Hausa_dict,
    "yoruba": yoruba_dict,
}



def nigerian_translator():

    print("==============================================")
    print("translator")
    print("==============================================")

    while True:
        print("\nhausa \nyoruba ")
        choice = input("Enter your language choice: ").strip().lower()

        if choice == 'quit':
            print("\nThank you for using the our Translator")
            break

        if choice in language_map:
            selected_dict = language_map[choice]
            print(f"\nYou have selected ---{choice.capitalize()}---.")
            
            english_word = input("Enter the English word to translate: ").strip().lower()

            if english_word in selected_dict:
                translation = selected_dict[english_word]
                print(f"\n----------------------------------------------")
                print(f" English: **{english_word.capitalize()}**")
                print(f"{choice.capitalize()}: **{translation}**")
                print(f"----------------------------------------------")
            else:
                print(f"\nSorry, the word **'{english_word}'** is not in the {choice.capitalize()} vocabulary.")
                print(f"Please try one of the following words: {', '.join(selected_dict.keys())}")

        else:
            print(f"\nInvalid language choice: '{choice}'. Please select from the list above.")

nigerian_translator()