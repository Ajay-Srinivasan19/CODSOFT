def display_menu():
    """
    Displays the main menu for the Career Guidance System.
    """
    print("\nWelcome to the Career Guidance Recommendation System!")
    print("1. Take a Skills Assessment")
    print("2. Explore Career Options")
    print("3. Get Detailed Career Information")
    print("4. Exit")


def skills_assessment():
    """
    Conducts a skills assessment to recommend a career path.
    """
    print("\nSkills Assessment: Answer the following questions to identify your career inclination.")
    
    questions = [
        ("Do you enjoy solving technical problems?", "Science and Technology"),
        ("Do you have a creative flair for writing, art, or design?", "Arts and Humanities"),
        ("Do you excel in managing finances or planning businesses?", "Commerce and Business"),
        ("Are you interested in helping others through medical or health services?", "Health and Medicine")
    ]
    
    scores = {
        "Science and Technology": 0,
        "Arts and Humanities": 0,
        "Commerce and Business": 0,
        "Health and Medicine": 0
    }
    
    for question, category in questions:
        while True:
            response = input(f"{question} (yes/no): ").strip().lower()
            if response == "yes":
                scores[category] += 1
                break
            elif response == "no":
                break
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")
    
    print("\nAssessment Complete!")
    recommended_category = max(scores, key=scores.get)
    print(f"Based on your responses, your recommended career path is: {recommended_category}")
    print("You can now explore careers or get detailed information in the main menu.")


def explore_career_options():
    """
    Displays career options for each category.
    """
    categories = {
        "Science and Technology": [
            "Software Developer", "Data Scientist", "Mechanical Engineer", "Cybersecurity Specialist"
        ],
        "Arts and Humanities": [
            "Graphic Designer", "Content Writer", "Social Worker", "Psychologist"
        ],
        "Commerce and Business": [
            "Accountant", "Investment Banker", "Entrepreneur", "Marketing Specialist"
        ],
        "Health and Medicine": [
            "Doctor", "Nurse", "Pharmacist", "Physiotherapist"
        ]
    }

    print("\nSelect an area of interest to explore career options:")
    for i, category in enumerate(categories.keys(), start=1):
        print(f"{i}. {category}")
    
    try:
        choice = int(input("\nEnter your choice (1-4): "))
        if 1 <= choice <= 4:
            category = list(categories.keys())[choice - 1]
            print(f"\nCareer options in {category}:")
            for career in categories[category]:
                print(f"- {career}")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")


def career_details():
    """
    Provides detailed information about specific careers.
    """
    career_info = {
        "Software Developer": "Designs and develops software applications. Requires proficiency in programming languages.",
        "Data Scientist": "Analyzes and interprets complex data to help organizations make informed decisions.",
        "Graphic Designer": "Creates visual content for branding, marketing, and communication.",
        "Psychologist": "Studies mental processes and helps individuals with mental health challenges.",
        "Investment Banker": "Provides financial services to clients, including raising capital and advisory services.",
        "Doctor": "Diagnoses and treats illnesses. Requires extensive education and training.",
    }

    print("\nAvailable Careers for Detailed Information:")
    for career in career_info.keys():
        print(f"- {career}")

    selected_career = input("\nType the name of the career exactly as shown above: ").strip()

    if selected_career in career_info:
        print(f"\nDetails for {selected_career}:")
        print(f"{career_info[selected_career]}")
    else:
        print("\nSorry, information for this career is not available. Please check your input and try again.")


def career_guidance_system():
    """
    Main function to run the Career Guidance Recommendation System.
    """
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                skills_assessment()
            elif choice == 2:
                explore_career_options()
            elif choice == 3:
                career_details()
            elif choice == 4:
                print("\nThank you for using the Career Guidance Recommendation System! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option (1-4).")
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    career_guidance_system()
