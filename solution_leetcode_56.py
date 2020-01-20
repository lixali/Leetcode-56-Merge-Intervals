### Given a collection of intervals, merge all overlapping intervals.
### 
### Example 1:
### 
### Input: [[1,3],[2,6],[8,10],[15,18]]
### Output: [[1,6],[8,10],[15,18]]
### Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
### Example 2:
### 
### Input: [[1,4],[4,5]]
### Output: [[1,5]]
### Explanation: Intervals [1,4] and [4,5] are considered overlapping.


### Time complexity is O(nlogn) because it is using built-in sort function
### Space complexity is O(n) because it is doing a linear comparison


### e.g input_list is [[4,6],[2,3],[5,10],[11,20]]
###     first, sort the input_list based on the first value(starting time) of each items in the list. Therefore, it becomes
###         [[2,3],[4,6],[6,10],[11,20]]
### 
###         2   3   (No overlapping with the next interval pair)
###         -----
###                 4       6   (there is overlapping here, [4,6] and [5,10] should becom [4,10])
###                 ---------
###                     5               10      (No overlapping with the next interval pair)
###                     ------------------
###                                         11                              20
###                                         ----------------------------------
###     Second, create a new list called final_intervals, and put the input_list first item in the final_intervals
###     Therefore, final_intervals becomes [[2,3]]
### 
###     Third, if the second value(ending time) of the last item in the final_interval is larger than first value(starting time) of next item in input_list,
###     it meas that there is overlapping, and then the final_intervals's last item ending time needs to be updated
###     Otherwise, it means that there is no overlapping. Therefore, append the interval pair to final_intervals
###     



class Solution():
    def mergeIntervals(self, input_list):
        sorted_intervals = sorted(input_list, key=lambda x: x[0])       ### sorted is O(nlogn) time complexity, using lambda expression to sort by the starting time (first value of each item in the list)
        print("After sorted by the first value of the each item in input_list, it becomes", sorted_intervals)
        final_intervals = [sorted_intervals[0]]         ### put the first interval pair in the final_intervals list, and use it to do comparison


        for i in range(1, len(sorted_intervals)):       ### if the length of input_list is 4, range(1,4) will be 1,2 and 3 
            if final_intervals[-1][1] >= sorted_intervals[i][0]:    ### If there is time overlapping here, update final_intervals's ending time
                final_intervals[-1][1] = max(final_intervals[-1][1],sorted_intervals[i][1] )
            else:
                final_intervals.append(sorted_intervals[i])     ### if there is no overlapping, the interval pair will be appended to final_interval list

        return final_intervals

input_list = [[4,6],[2,3],[5,10],[11,20]]
class_1 = Solution()
print("after merging the interval pairs, it becomes ", class_1.mergeIntervals(input_list))
