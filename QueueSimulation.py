import random
import os
import timeit
import time

# Simulate Queue with 2 counters
# To revert to 1 counter, remove reliance on start_time_2 and ellapsed_time_2
# Set initial variables to zero
old_customers = 0
total_time = 0
people_served = 0
people_left = 0


# Class of customers
class Customer:

    def __init__(self, time_taken):
        self.time_taken = time_taken


def print_board():  # Function to print main customer counter

    print '''
        ______________       _______________
        |            |       |             |
        | COUNTER 1  |       |  COUNTER 2  |
        |            |       |             |
        ______________       _______________
        '''


def print_customers(new, old):  # Function to print customers as required
    print ('''
                        <>
        ''') * (new + old)
    # old += new  # updating number of existing customers

start_time_1 = 0.0
start_time_2 = 0.0

# Main Loop
while True:
    os.system('CLS')
    print total_time
    print_board()
    new_customers = random.randint(0, 2)  # creating new customers
    print_customers(new_customers, old_customers)  # graphically displaying current customers in line
    old_customers = old_customers + new_customers

    # Simulate people leaving the line if line gets too long
    if old_customers >= 20 and random.randint(1, 5) == 2:
        old_customers -= 1
        people_left += 1
    else:
        pass

    if old_customers > 0:
        service_at_counter_1 = Customer(random.uniform(0.1, 0.3))  # Randomised time taken for each customer at counter
        service_at_counter_2 = Customer(random.uniform(0.1, 0.3))

        if start_time_1 > 0.0 or start_time_2 > 0.0:
            # each elapsed_time represents the time each customer has spent at the counter
            elapsed_time_1 = timeit.timeit() - start_time_1
            elapsed_time_2 = timeit.timeit() - start_time_2
            # Update start time
            start_time_1 = start_time_1 + timeit.timeit()
            start_time_2 = start_time_2 + timeit.timeit()

            if elapsed_time_1 >= service_at_counter_1 and old_customers > 0:
                old_customers -= 1
                people_served += 1
                start_time_1 = 0.0  # reset time
                # to visualise customers leaving line after service
                # print '''
                #                                   xx
                # '''
            if elapsed_time_2 >= service_at_counter_2 and old_customers > 0:  # Remove this function to change back to 1 counter simulation
                old_customers -= 1
                people_served += 1
                start_time_2 = 0.0  # reset time
            else:
                pass
        else:
            start_time_1 = start_time_1 + timeit.timeit()  # Update start time if elapsed_time isn't sufficient for
            start_time_2 = start_time_2 + timeit.timeit()  # customer to leave the line
    else:
        pass

    time.sleep(0.1)

    total_time += 0.1

    # Decide how long to run the simulation for
    if total_time >= 10:
        # Print out details about the simulation

        time.sleep(1)
        os.system('CLS')
        print total_time
        print_board()
        new_customers = 0
        print_customers(new_customers, old_customers)
        print "The Queue Simulation has run for %d seconds\n" % total_time
        print "We have served %d people and %d people left the line" % (people_served, people_left)
        print "There are still %d people in line" % old_customers
        print "Each customer took an average of %f seconds at the counter" % (total_time/people_served)
        break