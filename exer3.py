#test input for the algorithm
test_input = 22


#define a function that does the algorithm and takes a number as input
def algo(num):

    #save to answer_list all the shit that you get from the algorithm
    #as you can see the initial number was already placed inside the list
    answer_list = [num]

    #as long as the number is not one, it will keep going w the algorithm so it is a while loop hehe
    while num != 1:

        #if it is even, divide it by 2 then append what you got to the answer list
        if num % 2 == 0:
            num = num /2
            answer_list.append(int(num))

        #if it is anything else, which is odd i guess, then do the eq then append as well
        else:
            num = num*3 + 1
            answer_list.append(int(num))

    length = len(answer_list)

    #given that you have a list, you want to print it out as a string
    answer_string = ""

    #loop through all the numbers that you got then concatenate it into the string
    for i in answer_list:
        answer_string += str(i) + " "

    #this code is for removing the last space in your output so it doesn't have any bugs or something
    answer_string.rstrip()

    #print(answer_string)
    #print("This is the cycle-length " + str(length))
    return length


#run the function using the test input
algo(test_input)

def cycle_length(i, j):
    #initial is a list with both the inputs i and j in it
    initial = [i,j]

    #heres the list where im going to place them in order
    ordered_initial = []
    #i appended the minimum and maximum value to the empty list so that it is in order no matter what
    ordered_initial.append(min(initial))
    ordered_initial.append(max(initial))

    #to get the number of cycles
    n = ordered_initial[1] - ordered_initial[0]

    #where i will place all the lengths
    cycle_lengths = []

    #from 1 to n+2 because the range function excludes the last number and you want it to be included
    for i in range(1,n+2):

        #run the algo function before this then append to cycle_lengths
        one = algo(i)
        cycle_lengths.append(one)
    
    #print the maximum value of cycle_lengths list
    print(max(cycle_lengths))

cycle_length(1, 10)
cycle_length(200, 100)

        


    

        
        