import re

def get_live_data(query_type):
    """
    Provides hardcoded data for chatbot responses.
    This avoids the need for external API calls.
    """
    if query_type == "standings":
        # Hardcoded Premier League standings
        standings = [
            "1. Arsenal - 70 points",
            "2. Manchester City - 68 points",
            "3. Manchester United - 63 points",
            "4. Newcastle - 60 points",
            "5. Tottenham - 58 points"
        ]
        return "Premier League Standings:\n" + "\n".join(standings)

    elif query_type == "matches":
        # Hardcoded upcoming matches
        matches = [
            "Arsenal vs Chelsea - Saturday 3 PM",
            "Liverpool vs Manchester City - Sunday 5 PM",
            "Tottenham vs Newcastle - Monday 6 PM"
        ]
        return "Upcoming Matches:\n" + "\n".join(matches)

    elif query_type == "top_scorer":
        # Hardcoded top scorer information
        return "The current top scorer is Erling Haaland with 30 goals."

    else:
        return "Invalid query type. Please specify 'standings', 'matches', or 'top_scorer'."

def football_chatbot():
    """
    Main function for the Premier League Chatbot.
    Handles user queries with predefined responses.
    """
    print("Welcome to the Premier League Chatbot!")
    print("You can ask about standings, upcoming matches, top scorers, or specific team information.")
    print("Type 'exit' to leave the chatbot.\n")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for consistent handling
        
        if user_input == 'exit':
            print("Chatbot: Goodbye! Enjoy the beautiful game!")
            break
        
        # Handling Standings Query
        elif "standings" in user_input:
            response = get_live_data("standings")
            print(f"Chatbot: {response}")
        
        # Handling Upcoming Match Query
        elif re.search(r"(next|upcoming) match", user_input):
            response = get_live_data("matches")
            print(f"Chatbot: {response}")
        
        # Handling Top Scorer Query
        elif "top scorer" in user_input:
            response = get_live_data("top_scorer")
            print(f"Chatbot: {response}")
        
        # Handling Team Information
        elif re.search(r"team (.+)", user_input):
            team = re.search(r"team (.+)", user_input).group(1)  # Extract team name
            print(f"Chatbot: You asked about {team.title()}. Team information is currently static. Check back soon for updates.")
        
        # Handling Fixtures
        elif "fixture" in user_input:
            print("Chatbot: Fixtures are updated weekly. Would you like today's matches or a specific date?")
        
        # Default Response
        else:
            print("Chatbot: Sorry, I didn't quite catch that. Can you rephrase your question?")

# Entry point of the program
if __name__ == "__main__":
    football_chatbot()
