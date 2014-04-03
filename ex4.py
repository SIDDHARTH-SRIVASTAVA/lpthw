# number of cars
cars = 100
# number of seats for people in a car
space_in_a_car = 4.0
# number of people who can use cars, or wield them
drivers = 30
# number of people who take up 'space_in_a_car' (1.0 each) per car
passengers = 90
# the amount of cars unused because there aren't enough drivers
cars_not_driven = cars - drivers
# the amount of cars used because of the number of drivers
cars_driven = drivers
# total number of passengers we can carpool today
carpool_capacity = cars_driven * space_in_a_car
# how many passengers are in each car, on average
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Study Drills:"
print "0. Nothing above line 8 says what to do when encountering the variable "car_pool_capacity.""
print "1. If 4.0 was just 4, we'd be splitting people into fractions."
print "2. Floating point number means it can't be turned into a fractioned answer, I think. Everything has to be whole."
