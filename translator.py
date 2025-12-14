
Hausa_dictionary = {
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

igala_dictionary = {
    "hello": "kóo",
    "how are you": "chí là?",
    "i am fine": "mé jé gá", 
    "thank you": "àhì",
    "welcome": "gbàwó",
    "person": "ónú",
    "man": "ókùnrin",
    "woman": "ónògbá",
    "child": "ómí",
    "father": "àbà",
    "eat": "jé",
    "drink": "myí",
    "come": "wá",
    "go": "lo",
    "sleep": "wó",
    "water": "ómí",
    "house": "ulé",
    "food": "òúnjé",
    "hand": "òwó",
    "money": "óchí"
}

fulani_dictionary = {
    "hello": "no seenaa / a yawtii? (greeting/have you passed by?)",
    "how are you": "a jam-wolii? / no mbii'e?",
    "i am fine": "jam-wolii (I am well)",
    "thank you": "a jaaraama",
    "welcome": "sammba / a he'uɓɓe",
    "person": "gikku",
    "man": "gorko",
    "woman": "debbo",
    "child": "ɓiɗɗo",
    "father": "baaba",
    "eat": "nyaamde",
    "drink": "yarde",
    "come": "waru",
    "go": "yahu",
    "sleep": "ɗaanaade",
    "water": "ndiyam",
    "house": "saare / galle",
    "food": "nyaamdu",
    "hand": "junngo",
    "money": "ceede"
}

language = {
    "hausa": Hausa_dictionary,
    "yoruba": yoruba_dictionary,
    "igala": igala_dictionary,
    "fulani": fulani_dictionary,
    
}



def language():

    print("translator")

    while True:
        print("\nhausa \nyoruba \nigala \nfulani")
        choice = input("Enter your language choice: ").strip().lower()

        if choice == 'quit':
            print("\nThank you for using the our Translator")
            break

        if choice in language:
            selected_dictionary = language[choice]
            print(f"\nYou have selected ---{choice.capitalize()}---.")
            
            english_word = input("Enter the English word to translate: ").strip().lower()

            if english_word in selected_dictionary:
                translation = selected_dictionary[english_word]
                
                print(f" English: {english_word.capitalize()}")
                print(f"{choice.capitalize()}: {translation}")
                
            else:
                print(f"\nSorry, the word **'{english_word}'** is not in the {choice.capitalize()} vocabulary.")
                print(f"Please try one of the following words: {', '.join(selected_dictionary.keys())}")

        else:
            print(f"\nInvalid language choice: '{choice}'. Please select from the list above.")

language()