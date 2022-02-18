from FA import *
import os
import sys

print(""" \033[1m
  __  __       _   _                          _   _                __            
 |  \/  |     | | | |                        | | (_)              / _|           
 | \  / | __ _| |_| |__   ___ _ __ ___   __ _| |_ _  ___ ___     | |_ ___  _ __  
 | |\/| |/ _` | __| '_ \ / _ \ '_ ` _ \ / _` | __| |/ __/ __|    |  _/ _ \| '__| 
 | |  | | (_| | |_| | | |  __/ | | | | | (_| | |_| | (__\__ \    | || (_) | |    
 |_|  |_|\__,_|\__|_| |_|\___|_| |_| |_|\__,_|\__|_|\___|___/    |_| \___/|_|    
                                                                              
                                                                              
  _____                            _                  _____      _                     
 / ____|                          | |                / ____|    (_)                    
| |     ___  _ __ ___  _ __  _   _| |_ ___ _ __     | (___   ___ _  ___ _ __   ___ ___ 
| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|     \___ \ / __| |/ _ \ '_ \ / __/ _ \\
| |___| (_) | | | | | | |_) | |_| | ||  __/ |        ____) | (__| |  __/ | | | (_|  __/
 \_____\___/|_| |_| |_| .__/ \__,_|\__\___|_|       |_____/ \___|_|\___|_| |_|\___\___|
                      | |                                                           
                      |_|                                                         \033[0m""")

choseContinue= "Y"
while (choseContinue == 'Y'):
    print("\n\n🠗 List of all available automata 🠗\n")

    #Declaring the automaton files
    filesArray = os.listdir('Automata')

    #Initializing first position
    filePosition = 1

    #Printing all files for the user
    for file in filesArray:
        print(filePosition, ":",file)
        filePosition += 1

    #Emulating a do... while loop in python + secure INTEGER input
    isInvalid = True
    while isInvalid:
        isInvalid = False
        filePositionChosen = -1
        #Asking the user for the index of the chosen automata
        filePositionChosen = input("\nPlease Select a File (enter its position) : ")
        if (not filePositionChosen.isnumeric()):
            print("This is not a number !")
            isInvalid = True
        else:
            filePositionChosen = int(filePositionChosen)
            if (filePositionChosen < 1 or filePositionChosen > len(filesArray)):
                isInvalid = True
                print("Your number does not correspond to any file !")
      

    #Reading the chosen automata and displaying it before computation
    chosenFA = read_automaton_from_file(filesArray[filePositionChosen-1])
    print("\n\n🠗 You have chosen the following automata 🠗")
    chosenFA.display_automaton()

    #Different computation depending on the type of automata
    if chosenFA.is_an_asynchronous_automaton():
        print("\n\033[1m🠗 Determinization and Completion of an Asynchronous Automata 🠗")
        CDFA = chosenFA.determinization_and_completion_of_asynchronous_automaton()
    else:
        if chosenFA.is_deterministic():
            if chosenFA.is_complete():
                print("\n\033[1m➞ Your automata is already complete ! 🠔\033[0m")
                CDFA = chosenFA
            else:
                CDFA = chosenFA.completion()
        else:
            print("\n\033[1m🠗 Determinizarion and Completion of a Synchronous Automata 🠗\033[0m")
            CDFA = chosenFA.determinization_and_completion_of_synchronous_automaton()

    #Print CDFA automata
    print("\n\n\033[1m🠗 Your Complete Deterministic Finite Automata 🠗\033[0m")
    CDFA.display_automaton()

    #Print Minimized CDFA (MCDFA) automata
    print("\n\n\033[1m🠗 Your Minimized Complete Deterministic Finite Automata 🠗\033[0m")
    MCDFA = CDFA.minimization()
    MCDFA.display_automaton()
    print(MCDFA.dico_E)

    #Word recognition
    word = CDFA.read_word()
    while word != "end":
        CDFA.recognize_word(word)
        word = CDFA.read_word()

    #Complementary Language
    print("\n\n\033[1m🠗 Your complementary Finite Automata 🠗\033[0m")
    AComp = CDFA.complementary_automaton()
    AComp.display_automaton()
    word = AComp.read_word()
    while word != "end":
        AComp.recognize_word(word)
        word = AComp.read_word()

    #Standardization
    print("\033[1m\n\n🠗 Your standard Finite Automata 🠗\033[0m")
    ACompStd = CDFA.standard_automaton()
    ACompStd.display_automaton()
    word = ACompStd.read_word()
    while word != "end":
        ACompStd.recognize_word(word)
        word = ACompStd.read_word()


    #Ask the user if he wants to continue
    choseContinue = input("\n\n\nDo you want to continue ? [Y for yes]")