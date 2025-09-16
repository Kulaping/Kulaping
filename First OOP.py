

class q_in_balance:
    def __init__(self, balance=0):
        self.questions_with_answer = [
            {
                "question": "What does CPU stand for?",
                "choices": ["Central Process Unit", "Computer Processing Unit", "Central Processing Unit", "Control Processing Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which company developed the Android operating system?",
                "choices": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the brain of the computer?",
                "choices": ["Monitor", "CPU", "Keyboard", "Hard Drive"],
                "answer": "CPU"
            },
            {
                "question": "Which one is a web browser?",
                "choices": ["Windows", "Google Chrome", "Adobe", "Linux"],
                "answer": "Google Chrome"
            },
            {
                "question": "What does HTML stand for?",
                "choices": ["HyperText Machine Language", "HighText Markup Language", "HyperText Markup Language", "HyperTool Multi Language"],
                "answer": "HyperText Markup Language"
            }
        ]
        self.ques_round2 =  [
            {
                "question": "What does 'HTTP' stand for?",
                "choices": ["HyperText Transfer Protocol", 
                            "HighText Transfer Protocol", 
                            "HyperText Transmission Program", 
                            "Hyper Tool Transfer Protocol"],
                "answer": "HyperText Transfer Protocol"
            },
            {
                "question": "Which programming language is primarily used for iOS app development?",
                "choices": ["Java", 
                            "Python", 
                            "Swift", 
                            "Kotlin"],
                "answer": "Swift"
            },
            {
                "question": "What does GPU stand for in computer hardware?",
                "choices": ["General Processing Unit", 
                            "Graphical Performance Unit", 
                            "Graphics Processing Unit", 
                            "Graphic Program Utility"],
                "answer": "Graphics Processing Unit"
            },
            {
                "question": "What is the main function of a DNS in networking?",
                "choices": ["To store data", 
                            "To translate domain names to IP addresses", 
                            "To encrypt network traffic", 
                            "To manage network bandwidth"],
                "answer": "To translate domain names to IP addresses"
            },
            {
                "question": "Which of the following is a NoSQL database?",
                "choices": ["MySQL", 
                            "PostgreSQL", 
                            "MongoDB", 
                            "Oracle"],
                "answer": "MongoDB"
    }
]
    
        self.score = balance

    def plus_balance(self):
        for question_answers in self.questions_with_answer:
            print(f"\n{question_answers['question']}")

            for choice in question_answers['choices']:
                print(f"- {choice}")

            while True:
                user_input_1 = input("Your answer: ").strip()

                if user_input_1.isdigit():
                    print("Please try again.")
                    continue

                if user_input_1.lower() == question_answers['answer'].lower():
                    self.score += 5
                    print("Correct!")
                    print(f"Your balance is now: {self.score}")
                    break
                else:
                    print("Wrong!")
                    print(f"Your balance is still: {self.score}")
                    break


class Shop:
    def __init__(self):
        self.items = {
            "Dildo": 15,
            "Coffee": 5,
            "Paper": 5,
            "Hotdog": 5,
            "Water": 5,
            "Bag": 20,
        }

    def display_items(self):
        print("\nItems to Buy:")
        for item, price in self.items.items():
            print(f" {item} : {price} points")


class PurchasePoints(q_in_balance):
    def __init__(self):
        super().__init__()
        self.shop = Shop()

    def purchase(self):
        self.shop.display_items()
        print(f"\nYour balance: {self.score}")
        
    #while True:
       
        user_input_2 = input("Choose an Item: ").strip().title()

        if user_input_2 in self.shop.items:
            points = self.shop.items[user_input_2]

            if self.score >= points:
                self.score -= points
                print(f"\nYou bought {user_input_2} for {points} points.")
                print(f"Remaining balance: {self.score}")
            else:
                print("\nNot enough balance.")
        else:
            print("\nItem not found.") 
            
    
    def round_2(self):
      self.round2 = q_in_balance()
      
      while True:
        user_input_3 = input("Do you want to continue and increase your points? (Y/N): ").strip()
        
        if user_input_3.isdigit():
            print("Invalid Input.")
            continue
        
        if user_input_3.lower() == "y":
            for q2 in self.round2.ques_round2:
                  print(f"\n{q2['question']}")
                  for choice2 in q2['choices']:
                       print(f"- {choice2}")
        
                  while True:
                      user_input_4 = input("Your answer: ").strip()
          
                      if user_input_4.isdigit():
                         print("Invalid Input")
                         continue
        
                      if user_input_4.lower() == q2['answer'].lower():
                         self.score += 5
                         print("Correct!")
                         print(f"Your balance is now: {self.score}")
                         break
                      else:
                          print("Wrong!")
                      print(f"Your balance is still: {self.score}")
                      break     
            break
        else:
            print("OK!")
            break

            
player = PurchasePoints()      
#shop = Shop()
player.plus_balance()     
player.purchase()
player.round_2()  
player.purchase()

'''
class Tracker:
    def __init__(self):
        self.balance = 0
        self.user_name = ""
        self.items = {
            "Dildo": 15,
            "Coffee": 25,
            "Paper": 5,
            "Hotdog": 1,
            "Car": 5000,
            "House": 20000,
        }

    def get_user_name(self):
        while True:
            user_input = input("Enter Your Name: ").strip()
            if len(user_input) <= 2:
                print("Please enter a valid name.")
                continue
            if not all(char.isalpha() or char.isspace() for char in user_input):
                print("Please enter a valid name.")
                continue
            self.user_name = user_input
            print(f"Hi {self.user_name}")
            break

    def deposit(self):
        while True:
            try:
                user_input = int(input("Amount to Deposit (Up to $500,000): "))
                if user_input > 500000:
                    print("Deposit amount exceeds the limit of $500,000.")
                    continue
                self.balance += user_input
                print(f"Your balance is: ${self.balance}")
                break
            except ValueError:
                print("Invalid input. Please try again.")

    def show_items(self):
        print("\nItems to Buy:")
        for item, price in self.items.items():
            print(f" {item}: ${price}")

    def purchase(self):
        self.show_items()
        user_input = input("\nChoose an Item to Buy: ").strip().title()
        if user_input in self.items:
            price = self.items[user_input]
            if self.balance >= price:
                self.balance -= price
                print(f"You bought {user_input} for ${price}. Remaining balance: ${self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Item not found. Please try again.")

tracker = Tracker()
tracker.get_user_name()
tracker.deposit()
tracker.purchase()
'''