'''
This file include all Activity we work in the class
'''
#-------Activity one -----------
# name = input("Enter the the name :")
# age = input("Enter you age :")
# food = input("What is the food do you like :")
# his_story = f"Once upon a time, he have {age} years old, in a quaint little village nestled at the foot of a majestic mountain range, there lived a young girl named {name}. he had a heart as pure as the morning dew and a curious mind that hungered for adventure and he like {food} food"
# print(his_story)
#------- End -----------

#------ Activity two ---------
# x=4
# def y():
#     x=5
#     print(x)
# print(x)
# y()
# print(x)
#------ End --------------

#------ Activity three ---------
# fruit = ["apple","banana","orang"]
# for i in range(len(fruit)):
#     print(f"{i+1}  {fruit[i]}")
#------ End --------------

#------ Activity four ---------
# x=[]
# for number in range(1, 101):
#     if number % 2 != 0:  
#         x.append(number)
# print(x)
#------ End --------------

#------ Activity five ---------
# num = [x for x in range(100) if x % 2 != 0]
# print(num)
#------ End --------------

#------ Activity six ---------    
class CV:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
        print(f"Hello {name}\n Your CV Experience data is :")

    def set_bth(self, data):
        self.__set_bth = data

    def get_bth(self):
        return self.__set_bth

    def DisplayExperience(self):
        for e in self.experience:
            print("Company: " + e.Company)
            print("Job title: " + e.Job_title)
            print("From: " + e.fromDate)
            print("To: " + e.ToDate)
            print()

class Experience:
    def __init__(self, fromDate, ToDate, Company, Job_title):
        self.fromDate = fromDate
        self.ToDate = ToDate
        self.Company = Company
        self.Job_title = Job_title


ex = [
    Experience(
        fromDate="2020",
        ToDate="2023",
        Company="Abdaa Soft",
        Job_title="Developer Application"
    ),

    Experience(
        fromDate="2020",
        ToDate="2023",
        Company="AlNoor",
        Job_title="Frappe Application"
    )
]

g_cv = CV("Ghamdan Al-Yamani", experience=ex)
g_cv.DisplayExperience()
#------ End --------------

