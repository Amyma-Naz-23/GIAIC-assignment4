SENTENCE_START:str = "Panaversity is fun. I learned to program and used Python to make my  "

def main():
    noun:str = input("Enter a noun: ")
    verb:str = input("Enter a verb: ")
    adjective:str = input("Enter an adjective: ")
    adverb:str = input("Enter an adverb: ")

    sentence:str = SENTENCE_START + noun + verb + adjective + adverb
    print(sentence) 

if __name__ == "__main__":
    main()
            