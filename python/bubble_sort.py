import os

class Solution:
    
    def bubble_sort2(self, array):

        def recallable():
            for i in range(len(array)):
                try:
                    current = array[i]
                    next = array[i+1]
                except IndexError:
                    current = None
                    next = None
                try:
                    if current > next:
                        temp1 = array.pop(i)
                        temp2 = array.pop(i)
                        array.insert(i, temp2)
                        array.insert(i+1, temp1)
                except TypeError:
                    pass 
            
        while True:
            if array[0] > array[1]:
                recallable()
            else:
                break


        
        return array

if __name__ == '__main__':
    os.system("clear")
    s = Solution()
    print("expecting =>", [1, 2, 3, 4, 5])
    print(s.bubble_sort2([5, 4, 3, 2, 1]))  
    print()
    print("expecting =>", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
    print(s.bubble_sort2([5, 4, 3, 2, 1, 10, 9, 8, 7, 6]))
    print()
    print("expecting =>", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(s.bubble_sort2([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]))
