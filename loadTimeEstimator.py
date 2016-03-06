import sys

def loadTimeEstimator(sizes, uploadingStart, V):
    finish_time = [x for x in uploadingStart]
    t = [0 for x in uploadingStart]
    c = len(sizes)
    time_ = 0
    curr_time = uploadingStart[0]
    while (c > 0):
        index_of_uploading_start = [i for i, x in enumerate(uploadingStart) if x == curr_time + time_ and sizes[i] != 0 ]


        if len(index_of_uploading_start):
            speed = V/float(len(index_of_uploading_start))
        else:
            speed = V
        #print index_of_uploading_start
        for i in index_of_uploading_start:
            if sizes[i] > 0:
                sizes[i] = sizes[i] - speed
                finish_time[i] = finish_time[i] + 1
                t[i] = t[i] + 1

            uploadingStart[i] = uploadingStart[i] + 1
        time_ += 1
        c = len([x for x in sizes if x > 0])
    return finish_time

sizes = [21, 10]
uploadingStart = [100, 105]
V = 2

#print loadTimeEstimator(sizes, uploadingStart, V)
print loadTimeEstimator([20, 10], [1, 1], 1)
#print loadTimeEstimator([1, 1, 1], [10, 20, 30], 3)
