##
# Michael Forsythe & Matthew Womack
# Lab 2 Part C Task 1
# Reformat movie announcement
##

movie_one = "Star Wars: The Force Awakens"
lead_one = "Daisy Ridley"
lead_two = "John Boyega"
movie_two = "Dirty Grandpa"
lead_three = "Robert DeNiro"
lead_four = "Zac Efron"

message = "Today we have a great double feature at WCUmovies: \n\nToday’s leading movie is: " + \
    movie_one + "\n \t Starring: " + lead_one[0] + ". " + lead_one[6:] + " and " + lead_two[0] + \
        ". " + lead_two[5:] + "\n\nFollowed by: " + movie_two + "\n \t Starring: " + lead_four[0] + \
            ". " + lead_four[4:] + " and \n \t The Great " + lead_three +"!"

print(message)