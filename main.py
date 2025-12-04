# mashiqlar4_0412

# 1-mashq
nums = [1, 2, 4, 5, 7, 10, 13]
result = list(filter(lambda x: x % 3 == 1, nums))
print(result)


# 2-mashq
nums = [3, 5, 7, 10]
result = list(map(lambda x: (x*2 if x*2 <= 10 else (x*2) % 10), nums))
print(result)



# 3-mashq
words = ["salom", "python", "dunyo"]
result = list(map(lambda x: x.capitalize(), words))
print(result)


# 4-mashq
a = [2, 3, 4]
b = [1, 2, 3]
result = list(map(lambda x, y: x * y, a, b))
print(result)



# 5-mashq
nums = [-5, 3, -2, 7, 0, -1]
result = list(filter(lambda x: x < 0, nums))
print(result)

