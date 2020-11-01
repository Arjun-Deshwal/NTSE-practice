# knowing the alphabet numbering is an important part of NTSE. It can solve many questions using it
# This is a small programme just for this only
import random

print("This programme is just for the practice of alphabet numbering, I will ask quesions, if you give correct answer then one point will be added to your score.")

lis=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
queslimit=int(input("How many quesitons do you want me to ask:"))
score=0
k=0

while k<queslimit:
	alphabet=random.choice(lis)
	ans=int(input(f'Tell the numbering of {alphabet}:'))

	if ans==lis.index(alphabet)+1:
		print('You are correct! One point added to your score!')
		score+=1
		k+=1
		print(f"Your score is {score}")
		print(f'{queslimit-k} chances left.\n')

	else:
		print(f'Opps! It\'s wrong. It\'s {lis.index(alphabet)+1}')
		k+=1
		print(f"Your score is {score}")

		print(f'{queslimit-k} chances left\n')	

print(f"You scored {score} out of {queslimit}.")
