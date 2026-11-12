# Making faces

def main():
    text = input("What's your mood now? ")

    print(convert(text))

def convert(mood):

    # chaining two replace() method
    mood = mood.replace(":)", "😊").replace(":(", "😔")
    return mood

main()