#!/usr/bin/env python
# coding: utf-8

# In[ ]:


question_set = {
    'science': {
        1 : ['The Centre for Cellular and Molecular Biology is situated at?', 'Hyderabad', ['Patna', 'Jaipur', 'Hyderabad', 'Delhi']],
        2 : ['Where is the Railway Staff College located?', 'Vadodara', ['Pune' , 'Mumbai' , 'Vadodara' , 'Nashik']],
        3 : ['The territory of Porus who offered strong resistance to Alexander was situated between the rivers of?', 'Jhelum', ['Jhelum', 'Ravi', 'Sutlej', 'Godavari']],
        4 : ['The famous Dilwara Temples are situated in?', 'Rajasthan', ['Uttar Pradesh', 'Maharashtra', 'Rajasthan', 'Madhya Pradesh']],
        5 : ['Wadia Institute of Himalayan Geology is located at?', 'Dehradun', ['Dehradun', 'Kulu', 'Kohima', 'Mizoram']],
        6 : ['Poona pact was signed on?', '1930', ['1930', '1947', '1928', '1957']],
        7 : ['Bijapur is known for its?', 'Gol Gumbaz', ['Char Minar', 'Taj Mahal', 'Gateway', 'Gol Gumbaz']],
        8 : ['T20 is related to which sport?', 'Cricket', ['Golf', 'Football', 'Basket Ball', 'Cricket']],
        9 : ['The Battle of Plassey was fought in?', '1757', ['1777', '1769', '1778', '1757']]
    },
    'maths': {
        1 : ['For some integer n, the odd integer is represented in the form of?', '2n+1', ['n', 'n+1', '2n+1', 'None']],
        2 : ['HCF of 26 and 91 is?', '13', ['15' , '13' , '19' , '11']],
        3 : ['The addition of a rational number and an irrational number is equal to?', 'Irrational number', ['rational number', 'Irrational number', 'Both', 'None']],
        4 : ['The multiplication of two irrational numbers is?', 'Maybe rational or irrational', ['Maybe rational or irrational', 'irrational number', 'rational number', 'None']],
        5 : ['If set A = {1, 2, 3, 4, 5,…} is given, then it represents?', 'Natural numbers', ['Whole numbers', 'Natural numbers', 'Rational Numbers', 'Complex numbers']],
        6 : ['Which of the following triangles have the same side lengths?', 'Equilateral', ['Scalene','Isosceles',' Equilateral','None']],
        7 : ['Area of an equilateral triangle with side length a is equal to?','√3/4 a2',['√3/2a','√3/2a2','√3/4 a2','√3/4 a']],
        8 : ['Which of the following are not similar figures?','Isosceles triangles',['Isosceles triangles','Circles','squares','None']],
        9 : ['Which of the following is not a similarity criterion for two triangles?','ASA',['AAA','SAS','SSS','ASA']]
    }
}

level = {
            'e' : [7, 8, 9],
            'm' : [4, 5, 6],
            'h' : [1, 2, 3]
        }

count = 0

correct_answer = []

class quiz_app:
   
    def selected_option(ops):                          # Selection of option
        ans = input("Please select option: ")
        if ans == 'd':
            return ops[3]
        elif ans == 'c':
            return ops[2]
        elif ans == 'b':
            return ops[1]
        elif ans == 'a':
            return ops[0]
       
    def display_questions(question, options):             # Displaying question to user
        try:
            print ('Question: ' , question)
            print ('(a)' , options[0] , end=' ')
            print ('(b)' , options[1] , end=' ')
            print ('(c)' , options[2] , end=' ')
            print ('(d)' , options[3] )

        except KeyError :
            print ('Oops something went wrong!!')

    def get_question_answer_options(q_no, topic):         # Showing questions along with options
        que = question_set[topic][q_no][0]
        ans = question_set[topic][q_no][1]
        ops = question_set[topic][q_no][2]
        return que , ans , ops

    def verify_answer(selected_ans, ans):                # Checking the correct answer
        global count
        try :
            if selected_ans in ans:
                print ('Your answer is correct\n')
                count = count + 1
            else :
                print("Your answer is wrong")
                print ('This is correct answer:', ans)
                correct_answer.append(ans)

        except TypeError:
            print ('The selected option is not correct\n')

    def group_quiz(selected_group, topic):               # Displaying questions as per the selected topics
        for q_no in selected_group:
            que, ans, ops = quiz_app.get_question_answer_options(q_no, topic)
            quiz_app.display_questions(que, ops)
            selected_answer = quiz_app.selected_option(ops)
            quiz_app.verify_answer(selected_answer, ans)

    def show_correct_answers(topic, selected_group):     # Display of correct answer to user
        print('Correct answers are: ', correct_answer)
        
    
    def start():                                         #Start menu for user
        user_name=input("Kindly Login to take Quiz, Enter your name: ")
        mobile_no=input("Enter your mobile number: ")
        email_id=input("Enter your email_id: ")
        
        print ("\nHello ", user_name)
        print ("Welcome to Fun Quiz, let's begin: ")
        
        quiz_app.show_topics()                        #shows topics of quiz to user
        topic = input('Enter topic name to start quiz:')
        print("You have selected ", topic, ' for Quiz\n\n')
        
        diff = input ("Select difficulty level 'e' for easy, 'm' for moderate, 'h' for hard :")
        quiz_app.group_quiz(level[diff], topic)
        
        print('\n\n')
        print('Below is your detailed info:')
        print(user_name, "you have scored ", count)
        quiz_app.show_correct_answers(topic, diff)

        print('\n\n')
        print('Quiz taken:', topic)
        print('Score:', count)
        print('Quiz difficulty:', diff)


    def remove_question(topic):                   #Deleting the questions by superuser
        print(question_set[topic])
        print("Select question key to delete question from topic ", topic)
        delete_question =int(input("Kindly enter the question 'key' you want to delete:"))
        del question_set[topic][delete_question]
        print('\n\n')
        print('Question deleted successfully, below is updated list')
        print(question_set[topic])

        #update the level from the level dictionary
        
        h = level['h']
        h.remove(delete_question)
        level['h'] = h

        m = level['m']
        m.remove(delete_question)
        level['m'] = m

        e = level['e']
        e.remove(delete_question)
        level['e'] = e

    def add_question(topic):                             #Adding new questions to the question set by super user
        print("Operation on Topic:", topic)
        diff_level = input("Kindly enter e: for Easy \n Enter m: for Moderate \n Enter h: for Hard: ")
        question = input("Please enter new question: ")
        ans = input("Please enter answer: ")
        ans_op = input("Kindly enter options comma separated eg: a,b,c,d: ").split (',')
        
        que_ans = [question , ans, ans_op]
        question_set[topic][len(question_set[topic]) + 1] = que_ans
        
        if diff_level == 'h':
            level['h'].append(len(question_set[topic]))
        elif diff_level == 'e':
            level['e'].append(len(question_set[topic]))
        elif diff_level == 'm':
            level['m'].append(len(question_set[topic]))
        
        print('\n\n')
        print('Question added successfully')
        quiz_app.show_topics()
        print(question_set[topic])
        return diff_level , que_ans , ans_op

    def show_topics():
        print("*****************Below are Quiz topics*****************")
        for topic in question_set:
            print(topic)
   
    def delete_topics():
        try:
            quiz_app.show_topics()
            topic_name = input('Please enter topic name to be deleted')
            del question_set[topic_name]
            print('Topic deleted successfully')
            quiz_app.show_topics()

        except ValueError :
            print ("Kindly enter proper topic name")

    def edit_topics():
        try:
            quiz_app.show_topics()
            topic_name = input('Please enter topic name to be updated')
            new_topic_name = input('Please enter new topic name')
            sub_question_set = question_set[topic_name] 
            del question_set[topic_name]
            question_set[new_topic_name] = sub_question_set
            print('Topic updated successfully')
            quiz_app.show_topics()

        except ValueError :
            print ("Kindly enter proper topic name")

    def update_topics():
        quiz_app.show_topics()
        print('Hit 1 for adding new topic :')
        print('Hit 2 for deleting topic :')
        print('Hit 3 for updating topic :')
        print('Hit 4 to Quit :')
        topic_option = input('Please select any option: ')
        topic_option = int(topic_option)

        if topic_option == 1:
            newtopic = input("Enter topic name")
            question_set[newtopic] = {}
            quiz_app.add_question(newtopic)
        elif topic_option == 2:
            quiz_app.delete_topics()
        elif topic_option == 3:
            quiz_app.edit_topics()

while True:
    try :
        print ('\n****************HI THERE WELCOME TO FUN QUIZ*******************')
        print ('Kindly hit 1 for taking Quiz based on different Topic:')
        print ('Kindly hit 2 for SuperUser access:')
        print ('Kindly hit 3 for listing Quiz Topic')
        print ('Kindly hit 4 for Exit:')
        option = input('Please select any option:')
        option = int(option)
        
        if option == 1 :
            quiz_app.start()
        elif option == 2 :
            super_user = input ("Kindly enter super username:")
            if super_user == "aparna" :

                admin_option = 1
                while admin_option != 5 :
                    try :
                        print('\n***************Hi Super User',super_user,'**************')
                        print('Hit 1 for adding new question :')
                        print('Hit 2 for deleting question :')
                        print('Hit 3 for updating question :')
                        print('Hit 4 for CRUD topics menu:')
                        print('Hit 5 to Quit :')
                        admin_option = input('Please select any option: ')
                        admin_option = int(admin_option)
                        if admin_option == 1:
                            quiz_app.show_topics()
                            topic_for_adding_question = input('Enter topic name for adding question ')
                            quiz_app.add_question(topic_for_adding_question)
                            
                        elif admin_option == 2:
                            quiz_app.show_topics()
                            topic_for_remove_question = input('Enter topic name for deleting question ')
                            quiz_app.remove_question(topic_for_remove_question)
                            
                        elif admin_option == 3:
                            quiz_app.show_topics()
                            topic_update_ques = input('Enter topic name for updating question ')
                            print(question_set[topic_update_ques])
                            diff_level = input ("Kindly enter e: for Easy \n Enter m: for Moderate \n Enter h: for Hard")
                            update_question_key =int(input("Kindly enter the question 'key' you want to update:"))
                            question = input ("Please enter new question: ")
                            ans = input ("Please enter answer: ")
                            ans_op = input ("Kindly enter options comma separated eg: a,b,c,d: ").split (',')
                            question_set[topic_update_ques][update_question_key] = [question , ans, ans_op]
                            
                            print('\n\n')
                            print('Question updated successfully ')
                            print(question_set[topic_update_ques])
                            
                        elif admin_option == 4:
                            quiz_app.update_topics()
                            
                        elif admin_option == 5:
                            break
                            
                    except ValueError :
                        print (" ")

            else :
                print(super_user, "You do not have super user permission, kindly login with super user." )
                
        elif option == 3:
            quiz_app.show_topics()
            
        elif option == 4:
            exit()
            
    except ValueError :
        print("Please select correct option")


# In[ ]:




