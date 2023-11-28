

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
        """The result function shows the outcome of the electio

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

        print("Election candidates")

        for candidate in candidates:
            print(f"{candidate}")
        
        user_id = input("Enter your user ID: ")
        
        if not user_id.isdigit() or user_id != 8:
            print("Your user ID must be a digit of 8 values")
            continue
        choice =  input("Enter Candidate of your choice: ")
        if choice.lower() == "q":
            break
        Election.vote(choice, user_id)
    Election.result()

if __name__ == "__main__":
    main()
