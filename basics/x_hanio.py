

# This is to practice program to implement the tower of Hanio

def hanoi(disks, source_d, auxiliary_d ,target_d):
    if disks == 1:
        print('Move disk {} from disk {} to disk {}'.format(disks,source_d, target_d))
        return

    hanoi(disks-1, source_d,target_d , auxiliary_d )

    print("movr disk {} from disk {} to disk {} ".format(disks,source_d,target_d))

    hanoi(disks-1, auxiliary_d,source_d ,target_d )

#print('Enter the number of Disks :')

di = int(input("Enter the num of disks : "))

hanoi(di,'A','B','C')

