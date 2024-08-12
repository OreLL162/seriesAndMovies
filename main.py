import csv
from scraper import get_upcoming_items
from emailer import send_email
import config

def save_to_csv(upcoming_items, choice, category):
    filename = f"{choice}_{category}_upcoming.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Release Date', 'Rating'])
        for item in upcoming_items:
            writer.writerow([item['title'], item['release_date'], item['rating']])
    print(f"List saved to {filename}")

def main():
    # Loop to ensure a valid choice is entered
    while True:
        choice = input("Would you like to see new Movies or new Series? (Enter 'movies' or 'series'): ").strip().lower()
        if choice in ["movies", "series"]:
            break
        else:
            print("Invalid choice. Please enter 'movies' or 'series'.")

    while True:
        category = input("Enter your preferred category (e.g., Action, Animation, Comedy, Drama, Horror, Romance ..): ").strip().capitalize()
        if category in ["Drama","Adventure","Thriller","Action","Crime","Comedy","Mystery","Fantasy","War","Romance","Family","Animation","Sport","Horror","Music"]:
            break
        else:
            print("Invalid choice. Please enter a valid catrgory.")

    # Ask if the user wants to send the list via email
    while True:
        send_email_choice = input("Would you like to send the list via email? (Enter 'yes' or 'no'): ").strip().lower()
        if send_email_choice in ['yes', 'no']:
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    # Ask if the user wants to save the list to a CSV file
    while True:
        save_csv_choice = input("Would you like to save the list to a CSV file? (Enter 'yes' or 'no'): ").strip().lower()
        if save_csv_choice in ['yes', 'no']:
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    # Retrieve upcoming items based on the user's choice and category
    upcoming_items = get_upcoming_items(choice, category)
    
    # Keep only 10 items in the list
    upcoming_items = upcoming_items[:10]

    if upcoming_items:
        if save_csv_choice == 'yes':
            save_to_csv(upcoming_items, choice, category)
        
        if send_email_choice == 'yes':
            send_email(upcoming_items, choice, category)
    else:
        print(f"No upcoming {choice} found in the category '{category}'.")

if __name__ == "__main__":
    main()