#this imports exit from sys
from sys import exit
#this imports click and time for the loading bar
import click,time
#this imports sqlite 3
import sqlite3

#this sets the database
DATABASE = "dbsetup(original).db"

#prints a loading screen
def loading():
  print("     Loading.")
  #prints "Loading"
  print("⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛")
  #prints a loading bar
  time.sleep(1)
  #this command sets the interval between the previous command and the one after it
  click.clear()
  #this clears everything on the console
  print("     Loading..")
  print("⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛")
  time.sleep(1)
  click.clear()
  print("     Loading...")
  print("⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛")
  time.sleep(1)
  click.clear()
  print("     Loading.")
  print("⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛")
  time.sleep(1)
  click.clear()
  print("     Loading..")
  print("⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛")
  time.sleep(1)
  click.clear()
  print("     Loading...")
  print("⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛")
  time.sleep(1)
  click.clear()
  print("     Loading.")
  print("⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛")
  time.sleep(1)
  click.clear()
  print("     Loading..")
  print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛")
  time.sleep(1)
  click.clear()
  print("     Loading...")
  print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛")
  time.sleep(1)
  click.clear()
  print("    Game Ready!!")
  print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
  time.sleep(2)
  click.clear()
  print("Link")
  time.sleep(0.5)
  click.clear()
  print("Link.")
  time.sleep(0.5)
  click.clear()
  print("Link..")
  time.sleep(0.5)
  click.clear()
  print("Link...")
  time.sleep(0.5)
  click.clear()
  print("Link... Start!!")

#this deletes a question
#this creates the function delete_questions and recieves the variable QID
def delete_questions(QID):
  #this connects to the database
  db = sqlite3.connect(DATABASE)
  #this sets the cursor
  cursor = db.cursor()
  #this deletes a row from a table where QID equals (userinput)
  sql = "DELETE FROM questions WHERE QID = ?"
  #this executes the cursor
  cursor.execute(sql, (QID,))
  #this commits the changes to the database
  db.commit()
  #this closes the database
  db.close()

#This adds questions
def add_questions(question, correctanswer, option1, option2, option3, option4, difficulty):
  db = sqlite3.connect(DATABASE)
  cursor = db.cursor()
  #this inserts intp the table a question and sets the correct answer and all the options
  sql = "INSERT INTO questions (question, correctanswer, option1, option2, option3, option4, difficulty) VALUES (?, ?, ?, ?, ?, ?, ?)"
  cursor.execute(sql, (question, correctanswer, option1, option2, option3, option4, difficulty))
  db.commit()
  db.close()

#This updates questions
def update_questions(question, correctanswer, option1, option2, option3, option4, difficulty, QID):
  db = sqlite3.connect(DATABASE)
  cursor = db.cursor()
  #this updates questions- the correct answer, the options and the difficulty where the QID is equal to something.
  sql = "UPDATE questions SET question = ?, correctanswer = ?, option1 = ?, option2 = ?, option3 = ?, option4 = ?, difficulty = ?, WHERE QID = ?"
  cursor.execute(sql,(question, correctanswer, option1, option2, option3, option4, difficulty, QID,))
  db.commit()
  db.close()

def admin_mode():
  print("Welcome to Admin Mode. Please enter your username and your password. ")
  #this asks for a specific username
  username = input("Username:")
  #this asks for a specific password
  password = input("Password:")
  #this sets the username
  if username == ("AidanC"):
    #this sets the password
    if password == ("lachlanisasimp"):
      print("Admin Mode has been unlocked.")
      #this waits an amount of time (in seconds) before performing the next action
      time.sleep(1)
     
     
      print("What would you like to do today?")
      #this takes in input for the admin mode choices
      admin_choices = int(input("1. Delete Questions \n2. Add Questions \n3. Update Questions \n4. Exit Admin Mode \n"))
      while admin_choices != 4:
        if admin_choices == 1:
          #this takes input for delete questions and the user can choose what they want to delete.
          print("You are now going to: Delete Questions.")
          QID = int(input("What is the number ID of the question you would like to delete?"))
          delete_questions(QID)
          
        elif admin_choices == 2:
          #this takes input to add in a new question
          print("You are now going to: Add Questions")
          question = input("What is the question you would like to add?")
          correctanswer = input("What is the correct answer for your question?")
          option1 = input("What is your first answer option?")
          option2 = input("What is your second answer option?")
          option3 = input("What is your third answer option?")
          option4 = input("What is your last answer option?")
          difficulty = input("What is question's difficulty rating? \n e- Easy\n m- Medium\n h- Hard\n ex- Extreme\n")
          add_questions(question, correctanswer, option1, option2, option3, option4, difficulty)
          #This was testing that the database was being changed - it is
          
        elif admin_choices == 3:
          
          print("You are now going to: Update Questions")
          #this takes input from the user to find out what they would like to change in a question
          question = input("What is the question you would like to update?")
          correctanswer = input("What is the correct answer for your question?")
          option1 = input("What is your first answer option?")
          option2 = input("What is your second answer option?")
          option3 = input("what is your third answer option?")
          option4 = input("What is your last answer option?")
          difficulty = input("What is your question's difficulty rating? \n e- Easy\n m- Medium\n h- Hard\n ex- Extreme\n")
          QID = int(input("What is the QID of your question?"))
          #this sends the variable information to the function
          update_questions(question, correctanswer, option1, option2, option3, option4, difficulty, QID)
      
        elif admin_choices == 4:
          print("You are exitting Admin Mode.")
          return "yes"
        else:
          print("There are only 4 choices, please select from 1 to 4.")
        admin_choices = int(input("1. Delete Questions \n2. Add Questions \n3. Update Questions \n4. Exit Admin Mode \n"))
        
   


#this opens the main function where the main part of my quiz is stored
def main():
  global DATABASE
  loading()
  db = sqlite3.connect(DATABASE)
  cursor = db.cursor()
 
  
 
    #This sets the variable 'score' to 0 to begin- this variable keeps track of your score.
  score = 0
  #This sets the variable 'lives' to 10 to begin- this variable keeps track of your lives
  lives = 3
  #This sets the variable 'loopamt' to 0 to begin- this variable keeps track of the amount of times it has looped through.
  loopamt = 0
   #This prints out the welcome message and the user instructions.  
  print("Konichiwa, welcome to an anime themed quiz ~UwU~ \nIf you get 3 questions wrong, you fail the quiz. If not, you pass the quiz. \nIf you get all the questions right, there is a special reward!!! (Being vored by Raul the Fat Hispanic) \nTo answer each question, please input the letter (a, b, c, d) associated with the answer you have selected.")

  
    #Variable 'begin' equals the user input answer to the printed question.
    
    
  begin = input("Do you wish to play this quiz? Please answer with either 'yes' or 'no'. ").lower().strip()
  #this loops the code so that if they get mis-spell or something they can retry.
  while begin != ("yes"):
    if begin == ("no"):  
      print("Sayonara, have a good day.")
      exit(0)
    elif begin == ("admin"):
      begin = admin_mode()
    else:
      begin = input("There was an error. Rebooting...\nDo you wish to play this quiz? Please answer with either 'yes' or 'no'. ")
  #these allow the user to choose the level they wish to play at. Line 194 allows the user to give input.
  level = input("What level would you like to play at?\n 1. Easy\n 2. Medium\n 3. Hard\n 4. Extreme\n")
  #this states that if level = 1 then it will select all questions from the database named questions where the difficulty column is 'e'. Same goes for the rest of them. If level = 2, all questions where difficulty = m is selected.
  if level == "1":
    sql = "SELECT * FROM questions WHERE difficulty = 'e';"
    cursor.execute(sql)
    results = cursor.fetchall()
  if level == "2":
    sql = "SELECT * FROM questions WHERE difficulty = 'm';"
    cursor.execute(sql)
    results = cursor.fetchall()
  if level == "3":
    sql = "SELECT * FROM questions WHERE difficulty = 'h';"
    cursor.execute(sql)
    results = cursor.fetchall()
  if level == "4": 
    sql = "SELECT * FROM questions WHERE difficulty = 'ex';"
    cursor.execute(sql)
    results = cursor.fetchall()

  

  
  
  
  

  
   
      
      
 
  #prints the beginning message
  print("Hai, let's begin!!")
  time.sleep(2)
  click.clear()
  #while lives is more than 0, the code can run- if not, the while loop will break.
  while lives >= 0:
    if loopamt >= 5:
      #this breaks the while loop
      break
    elif lives <= 0:
      #this also breaks the while loop
      break
    for question in results:
        #This prints the question for the user to answer.
        print(question[1])
        for i in range(3, 7):
          print("[", question[i], "]", end= " ")
        answer = input()
        #This if statement states that if variable 'answer' in full lowercase is equal to the 'cor' of the question then print 'Correct'.
        if answer.lower() == question[2]:
          print("Correct!")
          #This adds 1 to the variable named score.
          score = score + 1
          print("Score =", score)
          print("Lives =", lives)
          print("The correct answer is", answer)
         #This adds one to variable loopamt 
          loopamt = loopamt + 1
          print("You have", 5 - loopamt, "questions to go!")
          time.sleep(2)
          click.clear()
          
        #Since everything except the correct answer is wrong, the else statement states that for every other answer, print 'incorrect'. 
        else:
          print("Incorrect...")
          #This subtracts one from the variable named 'lives'.
          lives = lives - 1
          print("Score =", score)
          print("Lives =", lives)
          #No matter if the answer was right or wrong, the amount of times it has looped through must keep going up as each question progresses.
          loopamt = loopamt + 1
          if loopamt != 1:
            print("You have", 5 - loopamt, "questions to go!")
            time.sleep(2)
            click.clear()
          elif loopamt == 1:
            print("You have", 5 - loopamt, "question left!")
            time.sleep(2)
            click.clear()
          #This if statement says that if lives is equal to or less than 0, do something.
          if lives <= 0:
            #This gives the 'Game over' message based on whether the if statement's condition was fulfilled. In this case, its when lives becomes less than or equal to 0.
            print("🅶 🅰 🅼 🅴  🅾 🆅 🅴 🆁 ,   🆈 🅾 🆄  🅷 🅰 🆅 🅴  🆁 🆄 🅽  🅾 🆄 🆃  🅾 🅵  🅻 🅸 🆅 🅴 🆂 ")
        
        if lives <= 0:
          #This breaks the 'for' loop.
          break
    #This if statement states that when the amount of times it has looped through equals 20, print the final score, congradulatory message, and the correct answe percentage.
    if loopamt == 5:
      print("Your final score is", score, "!")
      print("Congradulations on passing the quiz!!!")
      #Since there are 20 questions
      print("Your correct answer percentage is", score*20,"%")
      
      #These print a short message and a 'Weeb Level' based on your score.
     
      if score == 4:
        print("LMAO YOU GOT ONE OFF- ASIAN MOTHER WHIP YOU FOR ONLY 80%")
        print("Weeb Level- 🏮[̲̅L][̲̅o][̲̅w] [̲̅L][̲̅e][̲̅v][̲̅e][̲̅l] [̲̅A][̲̅s][̲̅i][̲̅a][̲̅n]🏮 \n")
      elif score == 5:
        print("How is this possible??? *Special Reward Unlocked!!*")
        print("Weeb Level- 😈😳😨🤩 S♥E♥N♥P♥A♥I♥ ♥O♥T♥A♥K♥U🤩😨😳😈")
        print("✨Special Reward✨ - https://www.youtube.com/watch?v=xvFZjo5PgG0 \n")    
    print("Game Over, press stop to stop the programme and press run to re-try.")

  #This closes the database.
  db.close()
#this calls the main function.
main()


    
    
  
  
      
