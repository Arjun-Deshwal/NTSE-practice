import random

print('Hello! I am a simple programme, I will ask you the square of numbers, if you will correct answers then one point will be added to your score.\n')

print('Now tell me from where till where you want me to ask the squares.')

fromm=int(input("From:"))
till=int(input("Till:"))
score=0

lis=[i for i in range(fromm,till+1)]

k=0
while k<10:
	num=random.choice(lis)
	ans=int(input(f"Tell the square of {num}:"))

	if ans==num*num:
		print('Your are correct!\n')
		score+=1
		k+=1
		print(f"Your score is {score}.\n")
		print(f"{10-k} questions left.\n")

	else:
		print(f"Oops it's wrong! It is {num*num}\n")
		print(f"Your score is {score}.\n")
		k+=1
		print(f"{10-k} questions left.\n")
			

print(f"You scored {score} out of 10!")



