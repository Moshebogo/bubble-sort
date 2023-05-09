class Solution:

    def bubble_sort1(self, array):
        return sorted(array)  
    
    def bubble_sort2(self, array):

        for i in range(len(array)):
            current = array[i]
            try:
                next = array[i+1]
            except IndexError:
                next = None
            try:
                if current > next:
                    temp1 = array[i:i+1]
                    temp2 = array[i+1:i+2]
                    x = array.pop(i+1)
                    print(x)
                    array.insert(i, temp2[0])
                 
            except TypeError:
                pass  
             
          

        return array

if __name__ == '__main__':
    s = Solution()
    # print("expecting =>", [1, 2, 3, 4, 5])
    print(s.bubble_sort2([5, 4, 3, 2, 1]))    
    x = 1