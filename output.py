import sys


def print_solution(cars_data, cars, file_name):
    sys.stdout = open('./result/output_'+file_name+'.txt', 'w')
    print(cars)
    for car in range(cars):
        print(len(cars_data[car]))
        for i in cars_data[car]:
            print(i)

if __name__ == '__main__':
    print_solution()
