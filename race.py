# create a list of tuples representing each participant in the race
participants = [
    ("John", "10:00:00", "10:45:30"),
    ("Alice", "10:05:15", "10:55:10"),
    ("Bob", "10:10:30", "11:10:45"),
    ("Kate", "10:15:45", "11:00:15")
]

# define a function to calculate the race time for a participant
def calculate_race_time(participant):
    start_time = datetime.strptime(participant[1], '%H:%M:%S')
    finish_time = datetime.strptime(participant[2], '%H:%M:%S')
    race_time = finish_time - start_time
    return race_time

# calculate the race time for each participant and print the results
for participant in participants:
    race_time = calculate_race_time(participant)
    print(f"{participant[0]} completed the race in {race_time}")
