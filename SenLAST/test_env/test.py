# import datetime
# YEAR = 2009
# DAY_OF_YEAR = 62
# d = datetime.date(YEAR, 1, 1) + datetime.timedelta(DAY_OF_YEAR - 1)
# print(d)

#
# import pandas as pd
#
#
# def date_to_nth_day(date, format='%Y-%m-%d'):
#     date = pd.to_datetime(date, format=format)
#     new_year_day = pd.Timestamp(year=date.year, month=1, day=1)
#     return (date - new_year_day).days + 1
#
#
# if __name__ == '__main__':
#     print(date_to_nth_day('2017-02-01'))

#
# def remove_duplicates():
#     t = ['a', 'b', 'c', 'd']
#     t2 = ['a', 'c', 'd']
#     for t in t2:
#         t.append(t.remove())
#     return t
#
# remove_duplicates()

name_list =['F:/Test_SENTINEL/selected/cloud_free\\S3A_LST_2019-04-15_20h58m_314_NIGHT_1km_utm32_etrs89.tif', 'F:/Test_SENTINEL/selected/cloud_free\\S3A_LST_2019-04-16_09h09m_321_DAY___1km_utm32_etrs89.tif',]
# # name_list = [2019, 89]
# hr_list = [9, 9]
min_list = [31, 9]
print(type(min_list))
print(type(name_list))
print(min_list[1])
# min_list = str(min_list)
print(min_list[1])
# print(type(name_list))
# for i in min_list:
#     print(name_list[i].find(min_list))
for i, tiff in enumerate(name_list):
    for j, min in enumerate(min_list):
        if min_list[j] in name_list[i]:
            print("True")
        else:
            print("False")
# for i in range (len(name_list)):
#     index_list = str(name_list[i])
#     print(index_list[59:62])
# print(any(x in name_list for x in min_list))

# import numpy as np
# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a[::-1])