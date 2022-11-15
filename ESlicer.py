def main():
    print("Welcome to my eMail Slicer")
    print("")

    email_input = input("Input your email address: ")

    (userName, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", userName)
    print("Domain: ", domain)
    print("Extension", extension)

main()