print("Welcome to the Atomic Structure Knowledge tester")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "How many protons do silver have?")
  print("   a) 43")
  print("   b) 44")
  print("   c) 47")
  print("   d) 53")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Try again"
    score -=1
  elif answer == "b":
    output = "Wrong. Try again"
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. Try again"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What period is mercury in?")
  print("   a) group 6")
  print("   b) group 7")
  print("   c) group 8")
  print("   d) group 9")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. Try again"
    score -=1
  elif answer == "c":
    output = "Wrong. Try again"
    score -=1
    
  elif answer == "d":
    output = "Wrong. Try again"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which element have 2 valence electrons?")
  print("   a) tungsten")
  print("   b) rubidium")
  print("   c) titanium")
  print("   d) strontium")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Try again"
    score -=1
  elif answer == "b":
    output = "Wrong. Try again"
    score -=1
  elif answer == "c":
    output = "Wrong. Try again"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz, hope you learnt something and had fun!")
  
