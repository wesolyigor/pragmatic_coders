# Hello recruiter! Please open python online compiler, for example this one (don't worry, there's no scam):

# https://www.programiz.com/python-programming/online-compiler/ 

# Nex print this code, click RUN and and follow the instructions in the right window. Good luck! 

def get_information():
    name = input("Enter name and surname of candidate: ")
    while name != "Igor Wesołowski":
        print("Wrong :( Please try again...")
        name = input("Enter your name (may be you know some of Igor...): ")

    company = input("Great! Now, enter name of your company: ")
    while company != "Pragmatic Coders":
        print("Ehh... Don't you know where are you working? Try agan...")
        company = input("Enter your company (e.g. Coca Cola): ")

    print("Hurray! New hired:", name)
    print("Company:", company)
    print("Call on 506539197")
    
get_information()

