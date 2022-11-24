#Write a method that takes an integer array and a desired sum. 
# The output will be pairs of numbers from the inputed integer array that equal that desired sum. 
# If there are no pairs that work, return 'unable to find pairs'

#need a result array 
#while the length of the original list is > 0:
    #pop a number from the list 
    #for each elem in the list, add it to the popped number. if the sum is equal to desired_sum, append a new array into the result array with the popped number and the element

def sum_pairs(list, desired_sum):
    answer = []
    new_list = []
    while len(list) > 0:
        popped_num = list.pop(0)
        for elem in list:
            if popped_num + elem == desired_sum:
                new_list = [popped_num, elem]
                answer.append(new_list)
    if len(answer) < 1: 
        return 'unable to find pairs'
    return answer


