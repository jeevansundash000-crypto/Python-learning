print("Bhai or bhauno aaba shap ko kaun bhanea ga crorepati kea Season-1 per swagat hai")
print("Aaj ki rat dhum dham honea bhala hea ")
print("Toh chaliye shuru karte hai")
print("or dhea khea kaun crorepati bhanea ga ")
print("Contested There will be 3 round and each round be difficult than before and each round you will be asked 5 Questions")
print("Each Questions 1 min times to answer")
print("So give carefully ")
print("First Round will be Deep understanding and wise Knowledge questions with rapid fire ")
print("Second Round will be Puzzle solving")
print("And the Third/final Round will be Spelling Contests")
print("Tho challea suru khar thea hea")
print("First Round:General Knowledge with rapid fire")
print("Contested There will be a questions show to you and you have to choose correct answer with before others can choose first ")
print("Choose any number:-")
print(1,2,3,4,5,6,7,8,9,10)
num = int(input("Choose any number:"))
if num==1:
    print("Ese sabal ki lea hea rs.5000")
    print("Sabal ese prakar hea: Nepal ki raj dhani ka par hea?.")
    a = input("Sabal leakhea:")
    print(a.lower())
    if "kathmandu" in a:
        print("Bhahat bharyea aab ko mil tha hea rs.5000")
    else:
        print("Dhuk khea shat khana phear ra ha hea khi aab nea glalat sabal dhi ya hea")
elif num==2:
    print("Your Question is: What's your aim/purpose in life?.")
    input("Write your answer:")
    print("You have got 5 points for this")
elif num==3:
    print("Your Question is: What's is the true definition of success?.")
    input("Write your answer:")
    print("You have got 4 points for this")
elif num==4:
    print("Your Question is: Why are you came in this earth?.")
    input("Write your answer:")
    print("You have got 2 points for this")
elif num==5:
    print("Your Question is : What will you do if you have 1 crore now?.")
    input("Write your answer:")
    print("You have got 5 points for this")
elif num==6:
    print("Your Question is: If you have last wise to say what's will it?.")
    input("Write your answer:")
    print("You have got 6 points for this")
elif num==7:
    print("Your Question is: When you feel lonely and close your eyes whom do you see?.")
    input("Write your answer:")
    print("You have got 5 points for this")
elif num==8:
    print("Your Question is: What's karma?.")
    input("Write your answer:")
    print("You have got 4 points for this")
elif num==9:
    print("Your Question is: Does humans being has limit for actions?.")
    input("Write your answer:")
    print("You have got 5 points for this")
elif num==10:
    print("Your Question is: If you have one heart to give to whom do you give?.")
    input("Write your answer:")
    print("You have got 8 points for this")
else:
    print("Out of options")