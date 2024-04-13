################################ 
# Tenzin Wangda
# Mechanical Engineering
# 02230274
################################ 
# REFERENCES
#https://youtu.be/LWdsF79H1Pg?si=Sm1PjE7lOY3eQ22T
#https://youtu.be/tvJl039okPM?si=lPJobWLatn1HkxjL
################################ 
# SOLUTION: 49524 
################################

#Retrieve Inpput File Function
def retrieve_input_file():
    return open('input_4_cap1.txt', 'r')

#Compute Total Score Function
def compute_total(file_handler):
    total_points = 0
    data_map = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}

    for line in file_handler:
        entry = line.strip()
        if entry in data_map:
            total_points += data_map[entry]
    
    print("Total score:", total_points)

#Invoke the Functions    
file_ptr = retrieve_input_file()
compute_total(file_ptr)
#Close the File
file_ptr.close()