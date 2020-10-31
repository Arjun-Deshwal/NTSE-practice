# knowing the alphabet numbering is an important part of NTSE. It can solve many questions using it
# This is a small programme just for this only
import random
print("This programme is just for the practice of alphabet numbering, I will ask 10 quesions, elif you give correct answer then one point will be added to your score.")

lis=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
score=0
k=0
while k<10:
	alphabet=random.choice(lis)
	ans=int(input(f'Tell the numbering of {alphabet}:'))

	if alphabet=="A" and ans==1:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="B" and ans==2:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="C" and ans==3:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="D" and ans==4:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="E" and ans==5:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="F" and ans==6:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="G" and ans==7:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="H" and ans==8:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="I" and ans==9:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="J" and ans==10:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="K" and ans==11:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="L" and ans==12:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="M" and ans==13:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="N" and ans==14:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="O" and ans==15:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="P" and ans==16:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="Q" and ans==17:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="R" and ans==18:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="S" and ans==19:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="T" and ans==20:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="U" and ans==21:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="V" and ans==22:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="W" and ans==23:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="X" and ans==24:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="Y" and ans==25:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	elif alphabet=="Z" and ans==26:
		print("Your answer is correct!")
		score+=1
		k+=1
		print(f"{10-k} chances left of 10.")
	else:
		print("Opps! It's wrong.")
		k+=1
		print(f'{10-k} chances left of 10')
print(f"You scored {score} out of 10.")
