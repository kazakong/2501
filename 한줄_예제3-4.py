import numpy as np

## 데이터 : [2017,2018,2019] 년도 연봉

alice = [99,101,103]
bob = [110,108,105]
tim = [90,88,85]


salaries = np.array([alice,bob,tim])
taxation = np.array([[0.2,0.25,0.22],
                     [0.4,0.5,0.5],
                     [0.1,0.2,0.1]])

max_income = np.max(salaries - salaries * taxation)
min_income = np.min(salaries)
print(max_income)
print(type(salaries))
print(min_income)
