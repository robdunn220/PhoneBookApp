import sys
import pickle

electronic_PB = open('phonebook.pickle', 'r')
phonebook_dict = pickle.load(electronic_PB)

#Function that iterates through the list electronic_PB, looking for a match for the user input.
def look_up():
    look_up_name = raw_input("Type a name to look up: ")

    #Displays information of contact if match is found
    for k in electronic_PB:
        if look_up_name == k:
            print "Name: %s" % k
            print "Phone number: %s" % electronic_PB[k]
            print "\n"
            break
        else:
            pass

    #Gives user the option to add new contact if a match is not found in the existing contents of electronic_PB
    for k in electronic_PB:
        if look_up_name != k:
            add_name = raw_input("Sorry, that name is not in the phone book. Add it (Y or N)? ")
            if add_name.upper() == 'Y':
                new_number = raw_input("What is their phone number? ")
                electronic_PB[look_up_name] = new_number
                print "\n"
                print "Entry has been made for %s" % look_up_name
                break
            else:
                phone_book()
            break

#Function that creates a new contact in electronic_PB based on user input
def set_up():
    new_name = raw_input("Type a name to add: ")

    #Ensures that the new contact the user wants to add does not already exist in electronic_PB
    for k in electronic_PB:
        if new_name != k:
            new_number = raw_input("What is their phone number? ")
            electronic_PB[new_name] = new_number
            print "\n"
            print "Entry has been made for %s" % new_name
            break
        else:
            print "Name has already been added. Back to menu."
            break

#Function that allows the user to delete an existing contacts in electronic_PB
def delete_entry():
    entry_to_del = raw_input("Type a name to delete: ")

    #Iterates through electronic_PB to find a match
    #If a match is found, it will be deleted from electronic_PB
    for k in electronic_PB:
        if entry_to_del == k:
            del electronic_PB[entry_to_del]
            print "\n"
            break

    print "Sorry, that name is not in the phone book."

def list_all():
    for k in electronic_PB:
        print "Name: %s" % (k)
        print "Number: %s" % (electronic_PB[k])
        print "\n"

def phone_book():
    print "\n"
    print "Electronic Phone Book"
    print "====================="
    print "1\. Look up an entry\n"
    print "2\. Set an entry\n"
    print "3\. Delete an entry\n"
    print "4\. List all entries\n"
    print "5\. Quit\n"
    usr_input = int(raw_input("What do you want to do (1-5)? "))
    print "\n"

    if usr_input == 1:
        look_up()
    elif usr_input == 2:
        set_up()
    elif usr_input == 3:
        delete_entry()
    elif usr_input == 4:
        list_all()
    elif usr_input == 5:
        print "Thank you for using Electronic Phone Book"
        sys.exit();

    while usr_input != 5:
        phone_book()

phone_book()
