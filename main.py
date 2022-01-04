import random
import time
print("Hello! I am a chatbot. Now we are going talk. \nWhat were you expecting for me to show you how to backflip:). \nIf you want to quit or converisation just write END as an answer.\n")
class Person():
    def __init__(self):
        self.name=str
        self.surname=str
        self.age=int
        self.job=str
        self.color=str
        self.adressing=str
        self.gender=str
        self.old = str
def getting_answer(question,topic):
    if topic == 0:
        answer= input("What is your "+question+"? ")
    elif topic == 1:
        if "past" in question:
            question = question.replace("past", "", 1)
            answer = input(person.adressing+" How was" + question + "?")
        elif "random" in question:
            question = question.replace("random","",1)
            a=question.split("?")
            input(a[0]+"? ")
            answer = input(a[1]+"? ")
        else:
            answer = input(person.adressing + " How is " + question + "? ")
    return answer
def recognising_answer(answer,topic,question):
    good_words=["GOOD","FINE","OKAY","BEAUTIFUL","WELL","AWESOME","PERFECT","AMAZING","BEST","WONDERFUL"]
    bad_words=["BAD","TERRIBLE","HORRIBLE","USELESS","WORSE","WORST"]
    positive_responds = ["That is great.","That is amazing.","That is good"]
    negative_responds = ["I am sorry to hear that.","That is bad."]
    neutral_responds=["okay","allright"]
    colors = ["red","green","white","blue","purple","gray","black","yellow","brown","orange","pink"]
    state=0
    goodword_presence = False
    badword_presence = False
    uppercase_answer=answer.upper()
    splitted_answer=uppercase_answer.split()
    wordnumber=0

    if topic==0:
        for word in splitted_answer:
            if word== "AM"or word=="IS"or word=="ARE"or word=="WAS" or word=="WERE"or word=="BE"or word=="BEEN":
                break
            wordnumber+=1
        exact_answer = splitted_answer[(wordnumber + 1)%len(splitted_answer)]
        if "surname" in question:
            person.surname = exact_answer.title()
            respond = "Okay."+person.name+" "+person.surname
        elif "name" in question:
            person.name = exact_answer.title()
            respond = "Hello "+person.name+". Nice to meet you."

        elif "age" in question:
            while True:
                try:
                    int(exact_answer)
                    person.age = int(exact_answer)
                    break
                except ValueError:
                    print("I could not get your age can you write it as just a number.")
                exact_answer = input()
            if person.age <=23:
                print("It is good to be young.")
                person.adressing = person.name
                person.old="young"
            else:
                print("Okay. You are older than I thought.")
                person.old = "old"
            gender = input(" What is your gender(male,female)")
            while gender!="male" and gender!="female":
                gender = input("I could not get it. Please choose one of them.(female, male)")
            person.gender = gender
            if person.old=="old":
                if person.gender=="female":
                    person.adressing = "Ms. "+person.surname
                else:
                    person.adressing = "Mr."+person.surname
            respond = "Okay. "+person.adressing+" nice to meet you again."
        elif "job"in question:
            person.job = exact_answer.lower()
            respond = "Okay. I don't know much about "+person.job+"; I am just a basic chatbot."
        elif "color"in question:
            person.color = exact_answer.lower()
            if person.color in colors:
                respond = "I know "+person.color+". It is a good color."
            else:
                respond = "I don't know "+person.color+"."






    elif topic==1:
        for word in splitted_answer:
            for good_word in good_words:
                if word==good_word:
                    state = 1
                    goodword_presence = True
            for bad_word in bad_words:
                if word == bad_word:
                    state= -1
                    badword_presence=True
            if len(splitted_answer)<=1:
                if ("not" in splitted_answer) or ("n" in splitted_answer[wordnumber - 1] and "t" in splitted_answer[wordnumber - 1] and "'" in splitted_answer[wordnumber - 1]):
                    state*=-1
            elif len(splitted_answer)>1:
                if ("not" in splitted_answer) or ("n" in splitted_answer[wordnumber - 1] and "t" in splitted_answer[wordnumber - 1] and "'" in splitted_answer[wordnumber - 1])or ("n" in splitted_answer[wordnumber - 2] and "t" in splitted_answer[wordnumber - 2] and "'" in splitted_answer[wordnumber - 2]):
                    state *= -1
            wordnumber+=1
        if badword_presence==True and goodword_presence == True:
            state = 0
        if state ==1:
            respond = random.choice(positive_responds)
        elif state == 0:
            respond = random.choice(neutral_responds)
        elif state ==-1:
            respond = random.choice(negative_responds)

    return respond


person = Person()
learning_questions = ["name","surname","age","job"]
spending_questions = ["past your day","your life","your family","your friend","weather outside","past weather yesterday","past school","your best friend","random What do you do in your free time?Why?","random Do you have hobbies?Why?","random What is your favorite sport?Why","random What is your favorite food?Why?","random When do you usually wake up?Why not earlier?","random When do you usually sleep?Why not earlier?","random What is your favorite drink?Why?"]
counter =0
counter_le=0
topic=0
while True:
    time.sleep(0.15)
    if counter >=3:
        if counter_le>=4:
            topic = 1
        else:
            topic = random.choice([0,1])
    if topic == 0 and counter_le<=4:
        question = learning_questions[counter_le]
        counter_le+=1
    elif topic==1 and len(spending_questions)>=1:
        question_number = random.randint(0, len(spending_questions)-1)
        question = spending_questions[question_number]
        spending_questions.remove(spending_questions[question_number])
    else:
        print("I am out of everything, but I realized something you like talking:) .\nBut I can not stop until you end the conversation; \nso I am going to listen you until you write END as an answer.")
        answers=["Okay!","Interesting!","Wow!","????","¯\_(ツ)_/¯","(͡°͜ʖ͡°)","Hmmm","Well","ohh","allright"]
        while True:
            answer = input("Explain me more about yourself.")
            if answer.upper()=="END":
                break
            print(random.choice(answers))
        print("Wow! that was a long talk.")
        break
    answer= getting_answer(question,topic)
    time.sleep(0.3)
    if answer.upper()== "END":
        break
    else:
        respond = recognising_answer(answer,topic,question)
        print(respond)
    counter +=1
print("That was a good talk.")