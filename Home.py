import time
import random
import mysql.connector

class Nzavote:
    def __init__(self, candidates, db_config):
        """Args:
        candidates ===> list of candidates for the election

        variable votes will initialized the value of each candidate to 0

        variable user records the unique ID of each user so that users/ voters
        don't vote twice. 
        """

        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}
        self.user_ids = set()
    
        # Initialize MySQL connection
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS election_results (
                candidate VARCHAR(255) PRIMARY KEY,
                votes INT
            )
        """)

        # Create second table for user_id
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Voters (
                VOTER_ID VARCHAR(255) UNIQUE
            )
        """)
    

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
            # Check if the user ID already exists in the Voters table
            self.cursor.execute("SELECT COUNT(*) FROM Voters WHERE VOTER_ID = %s", (user_id,))
            count = self.cursor.fetchone()[0]
            if count == 0:
                # User hasn't voted yet, proceed with the vote
                self.votes[candidate] += 1
                self.user_ids.add(user_id)

                # Insert the user's ID into the Voters table
                self.cursor.execute("INSERT INTO Voters (VOTER_ID) VALUES (%s)", (user_id,))
                print(f"\nUser: {user_id} voted successfully for {candidate}\n")
            else:
                print(f"\nUser {user_id} already voted, have a nice day while you wait for the results\n")
        else:
            print(f"\nInvalid candidate. Enter the correct candidate\n")


    def result(self):
        """The result function shows the outcome of the election

        example ===>

        Election Rsults:

        Omar: 1 Votes
        Chinedu: 5 Votes
        Nelson: 0 Votes

        -
        
        """
            # Execute SQL query to fetch election results from the database
        self.cursor.execute("SELECT candidate, votes FROM election_results")

    # Fetch all rows from the result set
        results = self.cursor.fetchall()

        print("\nElection Results:\n")
    
        for candidate, vote in results:
            print(f"{candidate}: {vote} Votes")
 

    def store_results_in_database(self):
        """Store election results in the MySQL database."""
        for candidate, vote in self.votes.items():
            self.cursor.execute("INSERT INTO election_results (candidate, votes) VALUES (%s, %s) ON DUPLICATE KEY UPDATE votes = votes + %s",
                                (candidate, vote, vote))
            
        self.connection.commit()




def main():


    """In this function we will call the Nzavote object and pass 
        list of candidates in it.

        Then we will make a while loop that will ask us to input our ID
        and the candidate we want to vote for. 

        The ID must be a digit of eight characters, 
         we will then use the ID as a parameter for our vote function(second Param)

        The candidate of choice will also be entered by the user and that will be the first parameter
    """
    candidates = ["Omar", "Kevin", "Chiedu", "Nelson", "Naima","Palvis"]


    """"Call The Object"""

  
        # ... (existing main function code)

    db_config = {
        'host': 'localhost',
        'user': 'omar',
        'password': 'mansaring',
        'database': 'Election_results',
        }
    
 

    Election = Nzavote(candidates, db_config)    
                
        

    while True:

        print("\nWelcome to Nzavote voting system!\nwe make election processes easy\nand fraud-free! Enter:\n \n1 - To Initialize The Voting Process\n2 - To Renew Voters Card\n3 - To See Results\n4 - Any Key to Exit")
        
        user_option = input("Choice: ")

        user_option = user_option.lower()

        if user_option == '1':


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
                    
            



            user_choice = int(input("\nNzavote Voting Page\nBefore we begin, pls select your country: \n1. Rwanda\n2. Nigeria\n3. Kenya\n4. Gambia\n5. Is your country not listed?: "))
            
            user_input(user_choice)
            '''
                A comprehensive list of other features our application would have asides voting e.g renewal and/or purchase
                of voters cards etcetera.
            '''
            time.sleep(2)
            print("Election candidates")

            for candidate in candidates:
                print(f"  {candidate}")
            
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
            choice =  input("Enter Candidate of your choice or \"q\" to exit:  ")
            if choice.lower() == "q":
                break
            Election.vote(choice, user_id)
        
            


        elif user_option == '2':
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
        elif user_option =='3':
            Election.result()
            break
        else:
            break
        Election.store_results_in_database()
    




        

    

if __name__ == "__main__":
    main()
