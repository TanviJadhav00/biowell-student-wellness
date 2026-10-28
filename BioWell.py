
def show_menu():
    print("\n===== BioWell =====")
    print("1. Breathing Exercise")
    print("2. Study Break Tips")
    print("3. Daily Wellness Tip")
    print("4. Exit")


def breathing_exercise():
    print("\nBreathing Exercise")
    print("Sit comfortably and relax.")
    print("Breathe in gently for 4 seconds.")
    print("Breathe out slowly for 4 seconds.")
    print("Repeat at your own comfortable pace.")


def study_break_tips():
    print("\nStudy Break Tips")
    print("- Stand up and stretch gently.")
    print("- Drink some water.")
    print("- Rest your eyes regularly.")
    print("- Take breaks between study sessions.")


def wellness_tip():
    print("\nDaily Wellness Tip")
    print("Maintain a regular sleep schedule.")
    print("Stay hydrated and make time to relax.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            breathing_exercise()
        elif choice == "2":
            study_break_tips()
        elif choice == "3":
            wellness_tip()
        elif choice == "4":
            print("Thank you for using BioWell!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
