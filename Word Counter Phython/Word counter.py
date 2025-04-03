def count_words():
    while True:
        # Prompt the user to enter a sentence or paragraph
        user_input = input("Enter a sentence or paragraph (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        # Check for empty input
        if not user_input.strip():
            print("You entered an empty string. Please enter some text.")
            continue
        
        # Initialize counters for words, alphabets, and numbers
        word_count = 0
        alphabet_count = 0
        number_count = 0

        # Split the input into words and count them
        words = user_input.split()
        word_count = len(words)

        # Count alphabets and numbers
        for word in words:
            for char in word:
                if char.isalpha():  # Check if the character is an alphabet
                    alphabet_count += 1
                elif char.isdigit():  # Check if the character is a number
                    number_count += 1

        # Display the counts
        print(f"Word count: {word_count}")
        print(f"Alphabet count: {alphabet_count}")
        print(f"Number count: {number_count}\n")
        
        # Prompt the user for another input
        print("Enter another sentence or paragraph, or type 'exit' to quit.")

# Run the function
count_words()
