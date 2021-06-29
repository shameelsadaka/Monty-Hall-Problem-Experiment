import random
import math

class Game:
	number_of_experiments_done = 0
	number_of_winnings_when_switch = 0
	number_of_winnings_when_stay = 0

	def test_case(self):
		doors = [0,1,2]

		# The Host puts the car behind a door
		the_door_in_front_of_car = random.choice(doors)

		# First guess by the guest - Completely Random
		door_guessed_by_the_guest = random.choice(doors)


		# Now the host is going to open a door
		choices_the_host_have = doors.copy()


		# which is not the selected by guest
		choices_the_host_have.remove(door_guessed_by_the_guest)
		

		# It should't be the door in front of car 
		if(the_door_in_front_of_car in choices_the_host_have):
			choices_the_host_have.remove(the_door_in_front_of_car)
		door_opened_by_host = random.choice(choices_the_host_have)
		


		# The guest switches the choice
		remaining_doors = doors.copy()
		remaining_doors.remove(door_guessed_by_the_guest)
		remaining_doors.remove(door_opened_by_host)

		# Only one door left to be 
		door_switched_into_by_the_guest = remaining_doors[0]



		if the_door_in_front_of_car == door_guessed_by_the_guest:
			self.number_of_winnings_when_stay += 1;

		if the_door_in_front_of_car == door_switched_into_by_the_guest:
			self.number_of_winnings_when_switch += 1;

		self.number_of_experiments_done += 1


	def run_experiments(self):		
		for i in range(10 ** 5):
			self.test_case()


if __name__ == "__main__":
	game = Game()
	game.run_experiments()

	print("Stay on the choice : Win probability : " + str(math.floor(game.number_of_winnings_when_stay/game.number_of_experiments_done * 100)))
	print("Switch The Door : Win probability : " + str(math.floor(game.number_of_winnings_when_switch/game.number_of_experiments_done * 100)))