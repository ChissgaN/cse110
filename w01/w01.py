print("Please enter the following information:")
    
    # Prompt for user input
first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")
    
    # Stretch challenge prompts
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
start_month = input("Month started: ")
advanced_training = input("Completed advanced training (yes/no): ")
    
    # Formatting the output
last_name_upper = last_name.upper()
job_title_title = job_title.title()
email_lower = email_address.lower()
    
    # Display the formatted ID card
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last_name_upper}, {first_name}")
print(f"{job_title_title}")
print(f"ID: {id_number}")
print()
print(email_lower)
print(phone_number)
print()
    
    # Display stretch challenge information with aligned columns
print(f"Hair: {hair_color:<15} Eyes: {eye_color}")
print(f"Month: {start_month:<15} Training: {advanced_training.capitalize()}")
print("----------------------------------------")