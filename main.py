# 1
a = ["python", "code", "java", "script", "html", "databas"]
print(a)

b = list(filter(lambda el: len(el) > 4 and el != "e", a))
print(b)

# 2
a = [5, 12, 7, 24, 9, 16, 3, 18, 11]
print(a)

b = list(filter(lambda el: el % 2 == 0 and el > 10, a))
print(b)

# 3
a = ["site.com", "test.org", "blog.uz", "info.org", "web.net"]
print(a)

b = list(filter(lambda el: el[-3] == "org", a))
print(b)

# 4
a = [12, 8, 24, 15, 36, 9, 48, 20, 72]
print(a)

b = list(filter(lambda el: el % 4 == 0 and el % 6 == 0, a))
print(b)

# 5
a = [25, 13, 45, 102, 305, 77, 85, 100, 95]
print(a)

b = list(filter(lambda x: str(x).endswith('5'),a))
print(b)

# 6
a = ["salom", "dunyo", "kitob", "oquvchi", "uy", "makta"]
print(a)

b = list(filter(lambda x: len(x) != 2, a))
print(b)
