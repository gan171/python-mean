# wap to find mean
print("This programs helps you to find mean")
choice1 = int(input("For ungrouped data press 1,for discrete data press 2,for continuous data press 3: "))
if choice1 == 1:
    obs = int(input("enter how many number of observation :"))
    list1 = []
    sum_freq = 0
    i = 1
    while i < obs + 1:
        a = int(input("enter observation:"))
        sum_freq += a
        list1.append(a)
        i += 1

    mean = sum_freq / obs

    print("You have entered ", list1)
    print("mean of given number is ", mean)

if choice1 == 2:
    x_obs = int(input("how many x values? "))
    list_x = []
    freq = []
    sum_freq = 0
    sum_list = 0
    i = 1
    while i < x_obs + 1:
        a = int(input("enter x values :"))
        list_x.append(a)
        b = int(input("enter freq :"))
        freq.append(b)
        sum_freq += b
        i += 1
    print("x-val entered by you", list_x)
    print("frequency entered by you", freq)

    for i in range(len(list_x)):
        sum_list = sum_list + (list_x[i] * freq[i])
    print("Mean of given data is", sum_list / sum_freq)

if choice1 == 3:
    class_obs = int(input("how many classes? "))
    up_limit = []
    low_limit = []
    freq = []
    cl_mark = []
    sum_freq = 0
    sum_list = 0
    i = 1
    while i < class_obs + 1:
        b = int(input("enter lower class limit values :"))
        low_limit.append(b)

        a = int(input("enter upper class limit values :"))
        up_limit.append(a)

        c = int(input("enter freq :"))
        freq.append(c)
        sum_freq += c
        i += 1
    print("lower limit entered by you", low_limit)
    print("upper limit entered by you", up_limit)
    print("frequency entered by you", freq)

    for i in range(len(up_limit)):
        cl_mark.append((up_limit[i]+low_limit[i])/2)
        sum_list = sum_list + (cl_mark[i] * freq[i])
    print("The class mark will be", cl_mark)
    print("Mean of given data is", sum_list/sum_freq)
    print("*****CODED BY GANESH*****")
