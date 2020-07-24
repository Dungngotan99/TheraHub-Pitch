#!/usr/bin/env python3
"""
Reads from output file to parse the variables 

"""
import sys

def main(argv):

	fileName = str(argv[0])

	bad_chars = ['\t','"', '\n', ',']

	with open('example.txt') as file:
		content = [line.rstrip('\n') for line in file]

	for x in range(len(content)):
		content[x] = ''.join(i for i in content[x] if not i in bad_chars) 

	BodyStart = 11
			
	HeaderLine = content[BodyStart + 5]
	LevelOne = content[BodyStart + 7]
	LevelTwo = content[BodyStart + 9]
	EndLine = content[BodyStart + 11]

	Lv1_stats = LevelOne.split(' ', 1 )
	Lv2_stats = LevelTwo.split(' ', 1 )
	final_time_Score_ID = EndLine.split(' ', 1 )
	final_Score_and_ID = final_time_Score_ID[1].split(' ', 1 )

	print("final score and ID:", final_Score_and_ID)


	gameType = HeaderLine
	Lv1_time = str(Lv1_stats[0])
	Lv1_score = str(Lv1_stats[1])
	Lv2_time = str(Lv2_stats[0])
	Lv2_score = str(Lv2_stats[1])
	finalTime = str(final_time_Score_ID[0])
	finalScore = str(final_Score_and_ID[0])
	user = str(final_Score_and_ID[1])


	print(gameType) 
	print(Lv1_time) 
	print(Lv1_score) 
	print(Lv2_time) 
	print(Lv2_score) 
	print(finalTime) 
	print(finalScore)
	print(user)

	file.close()

if __name__ == "__main__":
	main(sys.argv[1:])
			 


