import time
import random

class Nzavote:
    def __init__(self, candidates):
        """Args:
        candidates ===> list of candidates for the election

        variable votes will initialized the value of each candidate to 0

        variable user records the unique ID of each user so that users/ voters
        don't vote twice. 
        """

        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}
        self.user_ids = set()

    def vote(self, candidate, user_id):
        """Vote function takes in candidate user wanted to vote for and users ID
            if the ID is not 8 digits or not a number, we willl receive an error message

            if the ID is correct the user will proceed and vote for the candidate of his choice.
            \chinedu will write here

            if the user enters the wrong candidate, the user will receive another error message
        
        """


        if user_id in self.user_ids:
            print(f"\nUser {user_id} already voted, have a nice day while you wait for the results\n")

        elif candidate in self.candidates:
            self.votes[candidate] += 1
            self.user_ids.add(user_id)
            print(f"\nUser: {user_id} voted successfully for {candidate}\n")
        else:
            print(f"\nIn Valid candidate. Enter the correct candidate\n")

    def result(self):
        """The result function shows the outcome of the election

        example ===>

        Election Results:

        Omar: 1 Votes
        Chinedu: 5 Votes
        Nelson: 0 Votes

        -
        
        """
        print("\nElection Results:\n")
    
        for candidate, vote in self.votes.items():
            print(f"{candidate}: {vote} Votes")

def main():


    """In this function we will call the Nzavote object and pass 
        list of candidates in it.

        Then we will make a while loop that will ask us to input our ID
        and the candidate we want to vote for. 

        The ID must be a digit of eight characters, 
         we will then use the ID as a parameter for our vote function(second Param)

        The candidate of choice will also be entered by the user and that will be the first parameter
    """

    candidates = ["Omar", "Palvis", "Chinedu", "Nelson", "Kevin", "Naima"]

    """"Call The Object"""



    Election = Nzavote(candidates)      
            
        

    while True:

        print("\nWelcome to Nzavote voting system!\nwe make election processes easy\nand fraud-free! Enter:\n \nA - To Initialize The Voting Process\nB - To Renew Voters Card\nC - To See Results\n")
        
        user_option = input("Choice: ")

        user_option = user_option.lower()

        if user_option == 'a':


            def user_input(choice):
                choice = int(choice)
                if choice == 1:
                    print("Next page loading")
                elif choice == 2:
                    print("Next page loading")
                elif choice == 3:
                    print("Next page loading")
                elif choice == 4:
                    print("Next page loading")
                elif choice == 5:
                    print("Seems like our services have not reached your country just yet")
                
            '''
                For each of the next page loading, they represent a different country as seen from the demo.
                So the next page for each of them is to be similar i.e contain the various features the constitution 
                of such country has for its citizens in terms of electoral procedures. e.g the next page would include a 
                number of prompts, depending on the various kinds of services offered in each country for elections, ranging 
                from 1. Apply for Voter's Card 2. Renewal of Voter's Card 3. See Candidated(Presidential elections/Govermental 
                Elections) 4. Vote /this is where the current code we have worked on comes under 5. View Results /if results 
                aren't out yet, a good if statement will do the trick.
            '''
                    
            



            user_choice = int(input("\nWelcome to Nzavote voting system!\nwe make election processes easy\nand fraud-free!\nBefore we begin, pls select your country:\ \n1. Rwanda\n2. Nigeria\n3. Kenya\n4. Gambia\n5. Is your country not listed?: "))
            
            user_input(user_choice)
            '''
                A comprehensive list of other features our application would have asides voting e.g renewal and/or purchase
                of voters cards etcetera.
            '''
            time.sleep(2)
            print("Election candidates")

            for candidate in candidates:
                print(f"{candidate}")
            
            user_id = input("Enter your user ID: ")
            '''
                For this user ID it can't and shouldn't just be numbers. For example: the first 3 elements could
                stand for the first the letters of the person's country, since this voting system is to be launched
                across africa. e.g NIG07823 -- this can be a userid a valid one at that. NIG represents Nigeria, 078
                represents the 78th voter for the country nigeria, and 23 stands for 2023 elections. like that.
            '''
            if len(user_id) != 8:
                print("Your user ID must be a digit of 8 values")
                continue
            choice =  input("Enter Candidate of your choice: \n")
            if choice.lower() == "q":
                break
            Election.vote(choice, user_id)
        
            


        elif user_option == 'b':
            country = input("Please select your country:\n1. Rwanda\n2. Nigeria\n3. Kenya\n4. Gambia\nCountry: ")
            name = input("Enter your full name: ")
            previous_id = input("Enter Previous ID to renew: ")

            if len(previous_id) == 8:

                new_id = int(''.join(str(random.randint(0, 9)) for _ in range(5)))


                if country == "1":
                    print(f"\nVoters card successfully renewed:\nName: {name}\nNew_ID: RWD{new_id}\n")
                
                elif country == "2":
                    print(f"\nVoters card successfully renewed:\nName: {name}\nNew_ID: NIG{new_id}\n")

                elif country == "3":
                    print(f"\nVoters card successfully renewed:\nName: {name}\nNew_ID: KEN{new_id}\n")
                elif country == "4":
                    print(f"\nVoters card successfully renewed:\nName: {name}\nNew_ID: GMB{new_id}\n")

                else:
                    print("Your country not available")
            
            else:
                print("Please enter a correct ID of 8 digits")
        elif user_option =='c':
            Election.result()
            break




        

    

if __name__ == "__main__":
    main()
