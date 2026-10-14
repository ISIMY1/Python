##Access Checker 

## this is asking for the username, if the account is active, and if they have admin access. 
username = input("Enter your username: ")
account_active = input("Is your account active? (yes/no): ").lower()
is_admin = input("Are you an admin? (yes/no): ").lower()

##Asking if the account is active and if they are an admin then it will print admin access granted 
if account_active == "yes" and is_admin == "yes":
##Here we are printing the access message 
    print("Admin access granted for user: " + username)
##Here we are checking if the account is not admin access
elif account_active == "yes" and is_admin == "no":
## It will print out the standard user access granted message
    print("Standard user access granted for user: " + username)
else:
    print("Access denied.")