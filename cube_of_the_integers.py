#author__uy_thea
#section_bscpe_2-2
#date_october_2_2024

from array import * #import array

cube_arr = array('i',[]) #define a variable for the array

while True:
    try:
        number_of_values = int(input("Enter the number of values: "))

        for i in range(number_of_values):
            value = int(input("Enter a value: "))
            cube_arr.append(value)

        
        for j in cube_arr:
            print(f"The cube of {j} is {j**3}")
        
    except:
        print("Invalid Output")
        continue


#end_of_the_program  