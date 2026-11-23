class Students:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.caste = input("Enter student caste: ")
        self.age = input("Enter student age: ")
        self.address = input("Enter student address: ")
        self.grade = input("Enter student grade: ")
        self.contact_number = input("Enter student contact_number: ")
        self.guardian_name = input("Enter student guardian_name: ")
        self.email_id = input("Enter student email_id:")

    def details(self):
        print("Here is the details of student")
        print("Name of the student:", self.name, self.caste)
        print("Age:", self.age)
        print("Address:", self.address)
        print("Grade:", self.grade)
        print("Contact_number:", self.contact_number)
        print("Guardian_name:", self.guardian_name)
        print("Email.ID:", self.email_id)


while True:
    aa = Students()
    aa.details()
    with open("Record of student management.txt", "a") as f:
        f.write(f"Name of the student:{aa.name}\n")
        f.write(f"Age:{aa.age}\n")
        f.write(f"Address:{aa.address}\n")
        f.write(f"Grade:{aa.grade}\n")
        f.write(f"Contact_number:{aa.contact_number}\n")
        f.write(f"Guardian_name:{aa.guardian_name}\n")
        f.write(f"Email.ID:{aa.email_id}\n")
        f.write("------------------------------------------\n")

    a1 = input("Do you want to append more details: ")
    if a1.lower() == "yes":
        print("Thankyou")
        continue
    elif a1.lower() == "no":
        a2 = input("Do you want to store the data: ")
        if a2.lower() == "yes":
            with open("Record of student management.txt", "r") as f:
                print(f.read())
        else:
            print("Thankyou")
            break
