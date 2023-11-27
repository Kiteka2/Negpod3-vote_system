priimport json

class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def vote(self, candidate):
        if candidate in self.candidates:
            self.votes[candidate] += 1
            print(f"Vote for {candidate} recorded successfully.")
        else:
            print(f"Invalid candidate: {candidate}. Vote not recorded.")

    def display_results(self):
        print("\nElection Results:")
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")

    def save_results(self, filename="voting_results.json"):
        with open(filename, "w") as file:
            json.dump(self.votes, file)
        print(f"Results saved to {filename}.")

def main():
    candidates = ["Candidate A", "Candidate B", "Candidate C"]
    voting_system = VotingSystem(candidates)

    while True:
        print("\nCandidates:")
        for candidate in candidates:
            print(f"- {candidate}")

        voter_choice = input("\nEnter the name of the candidate you want to vote for (or 'exit' to end): ")
        if voter_choice.lower() == "exit":
            break

        voting_system.vote(voter_choice)

    voting_system.display_results()
    voting_system.save_results()

if __name__ == "__main__":
    main()
