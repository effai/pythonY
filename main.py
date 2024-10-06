# декоратори -  керінг, замикання, області видимості


# def wrapper():
#     x = 10 # nonlocal
#
#     def inner():
#         nonlocal x
#         x += 10
#         print(x)
#
#     inner()
#     print(x)
#
#
# wrapper()

# def outer(text):
#
#     def inner(name):
#         print(name, text)
#
#     return inner
#
# c = outer("Hello")
# c("Den")
# c("Alex")
# c("Nick")

# def broadcast(name, msg, prefix):
#     print(f"[{prefix}] {name}: {msg}")
#
# broadcast("Alex", "Hello", "Admin")
# broadcast("Alex", "Hello", "Admin")
# broadcast("Alex", "Hello", "Admin")

# def broadcast(name):
#     def set_prefix(prefix):
#         def set_msg(msg):
#             print(f"[{prefix}] {name}: {msg}")
#         return set_msg
#     return set_prefix
#
# # broadcast("Alex")("Admin")("Hello")
#
# adm_alex = broadcast("Alex")
# adm_alex("Admin")("Hello")
# adm_alex("Moder")("Hello")
# adm_alex("User")("Hello")

# import functools

# def wrapper(func):
#     def inner():
#         print("Start func.")
#         func()
#         print("End func.")
#     return inner
#
# def foo():
#     print("Do something..")
#
#
# i = wrapper(foo) # map sorted filter zip
# i()

# def second_dec(func):
#     def inner(*args, **kwargs):
#         print("Hello is second decor")
#         func(*args, **kwargs)
#     return inner
#
# def repeat(times):
#     def my_decor(func):
#         def inner(*args, **kwargs):
#             print("Start func.")
#             for i in range(times):
#                 func(*args, **kwargs)
#             print("End func.")
#         return inner
#     return my_decor
#
# @second_dec
# @repeat(5)
# def foo(msg):
#     print("Do something..", msg)
#
# print(foo("Hello"))

import django
# venv -- Віртуальне середовище






















