from sys import exit
import click,time

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
  
    


def main():
  loading()
 
    #This sets the variable 'score' to 0 to begin- this variable keeps track of your score.
  score = 0
  #This sets the variable 'lives' to 10 to begin- this variable keeps track of your lives
  lives = 10
  #This sets the variable 'loopamt' to 0 to begin- this variable keeps track of the amount of times it has looped through.
  loopamt = 0
   #This prints out the welcome message and the user instructions.  
  print("Konichiwa, welcome to an anime themed quiz ~UwU~ \nIf you get 10/20 questions wrong, you fail the quiz. If you get over 10 questions right, you pass the quiz. \nIf you get all 20 questions right, there is a special reward!!! (Being vored by Raul the Fat Hispanic) \nTo answer each question, please input the letter (a, b, c, d) associated with the answer you have selected.")
    #Variable 'begin' equals the user input answer to the printed question.
    
    
  begin = input("Do you wish to play this quiz? Please answer with either 'yes' or 'no'. ")
  while begin.lower() != ("yes"):
    if begin.lower() == ("no"):  
      print("Sayonara, have a good day.")
      exit(0)
  begin = input("There was an error. Rebooting...\nDo you wish to play this quiz? Please answer with either 'yes' or 'no'. ")
   
      
      
  #This if statement defines what happens when the user inputs 'no' begin.lower() == "no":
  
  #This if statement defines what happens when the user inputs 'yes'.
  
  print("Hai, let's begin!!")
  time.sleep(2)
  click.clear()
  #This is the dictionary name and the primary dictionary opener.
  quiz_questions = {
    #This is the question name and the secondary dictionary opener.
    "question_1": {
      #This is a question variable, and it is defined by the text after the colon.
      "question": "Who is the main protagonist in the popular anime Demon Slayer?",
      #These are the answers that the user will have to choose from - variable 'ans' is defined by what's on the right of the colon.
      "ans": ["a.Nezuko Kamado", "b.Tanjiro Kamado", "c.Zenitsu Agatsuma", "d.Inosuke Hashibira"],
      #This is the correct answer for the question.
      "cor": "b"
   #This closes the secondary dictionary opener.
    },
    "question_2" : {
      "question": "What Tailed Beast does Naruto have in the anime Naruto?",
      "ans" : ["a.Nine Tails", "b.Ten Tails", "c.Eight Tails", "d.One Tail"],
      "cor" : "a"
    },
    "question_3" : {
      "question" : "What is Anya's power in Spy X Family?",
      "ans" : ["a.Telepathy", "b.Super Strength", "c.Teleportation", "d.Mind Reading"],
      "cor" : "d"
    },
    "question_4" : {
      "question" : "Which One Piece villain ate the Chop Fruit?",
    "ans" : ["a.Croc", "b.Buggy", "c.Don Kreig", "d.Arlong"],
    "cor" : "b"
    },
    "question_5" : {
      "question" : "Which Hunter X Hunter character is the only survivor of the Kurta Clan?",
    "ans" : ["a.Leorio", "b.Gon", "c.Kurapika", "d.Killua"],
    "cor" : "c"
    },
    "question_6" : {
      "question" : "In Haikyuu!, which school does Karasuno have a long standing rivalry with?",
    "ans" : ["a.Aoba Johsai", "b.Nekoma", "c.Fukurodani", "d.Itachiyama"],
    "cor" : "b"
    },
    "question_7" : {
      "question" : "Which Initial D: First Stage character drives a red Honda Civic?",
    "ans" : ["a.Takumi Fujiwara", "b.Shingou Shoji", "c.Natsuki Mogi", "d.Mako Sato"],
    "cor" : "b"
    },
    "question_8" : {
      "question" : "Which one of these is Yuji Itadori's power in Jujutsu Kaisen?",
    "ans" : ["a.Black Flash", "b.Infinity", "c.Dismantle", "d.Ratio"],
    "cor" : "a"
    },
    "question_9" : {
      "question" : "Which Food Wars character specialises in the cooking and handling of expensive meats?",
    "ans" : ["a.Ikumi Mito", "b.Satoshi Ikkishi", "c.Erina Nakiri", "d.Yukihira Soma"],
    "cor" : "a"
    },
    "question_10" : {
      "question" : "Which season of Shingeki no Kyojin uses 'Shinzo Wa Sasageyo' as it's opening?",
    "ans" : ["a.Season 1", "b.Season 2", "c.Season 3", "d.Season 4"],
    "cor" : "b"
    },
    "question_11" : {
      "question" : "What was the name of the gym that Brock leads in the anime Pokemon?",
    "ans" : ["a.Golden Gym", "b.Carbon Gym", "c.Pewter Gym", "d.Telekinesis Gym"],
    "cor" : "c"
    },
    "question_12" : {
      "question" : "Which Boku no Hero Academia character uses the quirk 'Hellflame'?",
    "ans" : ["a.Deku", "b.Gravity Girl", "c.Endeavour", "d.Red Riot"],
    "cor" : "c"
    },
    "question_13" : {
      "question" : "In Assassination Classroom, who used a giant pudding in an attempt to kill Koro Sensei?",
    "ans" : ["a.Nagisa Shiota", "b.Karma Akabane", "c.Kaede Kayano", "d.Itona Horibe"],
    "cor" : "c"
    },
    "question_14" : {
      "question" : "In Sword Art Online, what was Kirito's cousin, Suguha's in-game username in Alfheim Online?",
    "ans" : ["a.Leafa", "b.Nyanda", "c.Mizushi", "d.Tenri"],
    "cor" : "a"
    },
    "question_15" : {
      "question" : "In Violet Evergarden, how fast can Violet type in characters per second?",
    "ans" : ["a.300", "b.200", "c.100", "d.50"],
    "cor" : "b"
    },
    "question_16" : {
      "question" : "In Re-Zero, what magic type does Subaru use?",
    "ans" : ["a.Yang", "b.Ice", "c.Water", "d.Yin"],
    "cor" : "d"
    },
    "question_17" : {
      "question" : "In Ao Ashi, what soccer position does star player Haruhisa Kuribayashi play? ",
    "ans" : ["a.Full Back", "b.Midfielder", "c.Left Striker", "d.Centre Defense"],
    "cor" : "b"
    },
     "question_18" : {
      "question" : "In Darling In the Franxx, what was Hiro's code number? ",
    "ans" : ["a.001", "b.007", "c.012", "d.016"],
    "cor" : "d"
    },
     "question_19" : {
      "question" : "In Black Clover, what grimoire did the Wizard King Julius Novachrono possess?",
    "ans" : ["a.Time", "b.Gravity", "c.Nuclear", "d.Particle"],
    "cor" : "a"
    },
     "question_20" : {
      "question" : "In Classroom of the Elite: Season 2, what group is Ayanokoji placed in during a special test on board the cruise ship?",
    "ans" : ["a.Saturn", "b.Neptune", "c.Mars", "d.Mercury"],
    "cor" : "c"
    },
    
    #This closes the primary dictionary.
  }
  while lives >= 0:
    if loopamt >= 20:
      break
    elif lives <= 0:
      break
    for _ , question in quiz_questions.items():
        #This prints the question for the user to answer.
        print(question.get("question"))
        answer = input(question.get("ans"))
        #This if statement states that if variable 'answer' in full lowercase is equal to the 'cor' of the question then print 'Correct'.
        if answer.lower() == question.get("cor"):
          print("Correct!")
          #This adds 1 to the variable named score.
          score = score + 1
          print("Score =", score)
          print("Lives =", lives)
          print("The correct answer is", answer,".")
         #This adds one to variable loopamt 
          loopamt = loopamt + 1
          if loopamt != 1:
            print("You have", 20 - loopamt, "questions to go!")
            time.sleep(2)
            click.clear()
          elif loopamt == 1:
            print("You have", 20 - loopamt, "question left!")
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
  #This 'else' covers everything else apart from the answers 'yes' and 'no' as defined in lines 12 and 15.
    print("Game Over, press stop to stop the programme and press run to re-try.")

main()


    
    
  
  
      
