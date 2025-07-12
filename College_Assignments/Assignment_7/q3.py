# Function to extract username and domain from email
def extract_email_details(email):
    # Split the email by '@' to separate username and domain
    username, domain = email.split('@')
    return (username, domain)

# Input: email address from the user
email = input("Enter your email address: ")

# Get the tuple of username and domain
email_details = extract_email_details(email)

# Output the tuple
print(f"User-name and Domain tuple: {email_details}")
