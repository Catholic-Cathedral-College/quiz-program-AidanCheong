from sys import exit
import click,time
import sqlite3

DATABASE = "quizquestions.db"

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
  
    
def admin_mode():
  print("Welcome to Admin Mode. Please enter your username and your password. ")
  username = input("Username:")
  password = input("Password:")
  if username == ("AidanC"):
    if password == ("lachlanisasimp"):
      print("Admin Mode has been unlocked.")
      time.sleep(1)
      print("What would you like to do today?")
      admin_choices = int(input("1. Delete Questions \n2. Add Questions \n3. Exit Admin Mode"))
      if admin_choices == 1:
        print("You are now going to: Delete Questions.")
      elif admin_choices == 2:
        print("You are now going to: Add Questions")
        
      elif admin_choices == 3:
        print("You are exitting Admin Mode.")
        return "yes"
        
   
  

def main():
  global DATABASE
  #loading()
  db = sqlite3.connect(DATABASE)
  cursor = db.cursor()
  sql = "SELECT * FROM questions;"
  cursor.execute(sql)
  results = cursor.fetchall()
 
    #This sets the variable 'score' to 0 to begin- this variable keeps track of your score.
  score = 0
  #This sets the variable 'lives' to 10 to begin- this variable keeps track of your lives
  lives = 10
  #This sets the variable 'loopamt' to 0 to begin- this variable keeps track of the amount of times it has looped through.
  loopamt = 0
   #This prints out the welcome message and the user instructions.  
  print("Konichiwa, welcome to an anime themed quiz ~UwU~ \nIf you get 10/20 questions wrong, you fail the quiz. If you get over 10 questions right, you pass the quiz. \nIf you get all 20 questions right, there is a special reward!!! (Being vored by Raul the Fat Hispanic) \nTo answer each question, please input the letter (a, b, c, d) associated with the answer you have selected.")
    #Variable 'begin' equals the user input answer to the printed question.
    
    
  begin = input("Do you wish to play this quiz? Please answer with either 'yes' or 'no'. ").lower().strip()
  while begin != ("yes"):
    if begin == ("no"):  
      print("Sayonara, have a good day.")
      exit(0)
    elif begin == ("admin"):
      begin = admin_mode()
    else:
      begin = input("There was an error. Rebooting...\nDo you wish to play this quiz? Please answer with either 'yes' or 'no'. ")
  
   
      
      
  #This if statement defines what happens when the user inputs 'no' begin.lower() == "no":
  
  #This if statement defines what happens when the user inputs 'yes'.
  
  print("Hai, let's begin!!")
  time.sleep(2)
  click.clear()
  while lives >= 0:
    if loopamt >= 20:
      break
    elif lives <= 0:
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
          print("You have", 20 - loopamt, "questions to go!")
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
            print("You have", 20 - loopamt, "questions to go!")
            time.sleep(2)
            click.clear()
          elif loopamt == 1:
            print("You have", 20 - loopamt, "question left!")
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
    if loopamt == 20:
      print("Your final score is", score, "!")
      print("Congradulations on passing the quiz!!!")
      print("Your correct answer percentage is", score*5,"%")
      print("The answer key is... \n 1)b.Tanjiro Kamado \n 2)a.Nine Tails \n 3)d.Mind Reading \n 4)b.Buggy \n 5)c.Kurapika \n 6)b.Nekoma \n 7)b.Shingou Shoji \n 8)a.Black Flash \n 9)a.Ikumi Mito \n 10)b.Season 2 \n 11)c.Pewter Gym \n 12)c.Endeavour \n 13)c.Kaede Kayano \n 14)a.Leafa \n 15)b.200 \n 16)d.Yin \n 17)b.Midfielder \n 18)d.016 \n 19)a.Time \n 20)c.Mars")
      #These print a short message and a 'Weeb Level' based on your score.
      if score == 11:
        print("Phew, you just passed the quiz.")
        print("Weeb Level- 🌿ɢʀᴀꜱꜱ ᴛᴏᴜᴄʜᴇʀ🌿")
      #Elif = 'else if'. So basically the language is saying 'else if the score equals to 12, print short message and weeb level'. Elif is used between an if statement and an else statement as an additional if statement.
      elif score == 12:
        print("Close, but you still made it!")
        print("Weeb Level- 📱𝔜𝔬𝔲𝔗𝔲𝔟𝔢 𝔄𝔫𝔦𝔪𝔢 𝔚𝔞𝔱𝔠𝔥𝔢𝔯📱")
      elif score == 13:
        print("You have more animes to watch- what are you doing here?")
        print("Weeb Level- 🎉Ⓟⓞⓟⓤⓛⓐⓡ Ⓐⓝⓘⓜⓔⓢ Ⓞⓝⓛⓨ🎉" )
      elif score == 14:
        print("You have a pretty average anime count, eh?")
        print("📲Weeb Level- (っ◔◡◔)っ ♥ KEEᑭ ᗯᗩTᑕᕼIᑎG ♥📲")
      elif score == 15:
        print("Not bad...")
        print("Weeb Level- 😌𝐼𝓂𝓅𝓇♡𝓋𝑒𝒹 😌 \n")
      elif score == 16:
        print("You're pretty well watched, aren't you?")
        print("Weeb Level- 😁𝒮𝑒𝒶𝓈💮𝓃𝑒𝒹 𝒜𝓃𝒾𝓂𝑒 𝒲𝒶𝓉𝒸𝒽𝑒𝓇😁 \n")
      elif score == 17:
        print("Well, you're pretty close- watch a couple more and you'll nail it!")
        print("Weeb Level- 🥺丂乇几卩卂丨🥺 \n")
      elif score == 18:
        print("Ooh... two away... you're very close!")
        print("Weeb Level- 😤卂ⒹⒹ𝐈ĆⓉＥ𝔡 😤 \n")
      elif score == 19:
        print("LMAO YOU GOT ONE OFF- ASIAN MOTHER WHIP YOU FOR ONLY 95%")
        print("Weeb Level- 🏮[̲̅L][̲̅o][̲̅w] [̲̅L][̲̅e][̲̅v][̲̅e][̲̅l] [̲̅A][̲̅s][̲̅i][̲̅a][̲̅n]🏮 \n")
      else:
        print("How is this possible??? *Special Reward Unlocked!!*")
        print("Weeb Level- 😈😳😨🤩 S♥E♥N♥P♥A♥I♥ ♥O♥T♥A♥K♥U🤩😨😳😈")
        print("✨Special Reward✨ - https://www.youtube.com/watch?v=xvFZjo5PgG0 \n")    
    print("Game Over, press stop to stop the programme and press run to re-try.")

main()


    
    
  
  
      
