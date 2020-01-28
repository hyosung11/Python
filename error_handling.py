# Error Handling

# 1.
# while True:
#     try:
#         age = int(input('What is your age? '))
#         10/age
#     except ValueError:
#         print('Please enter a number')
#     except ZeroDivisionError:
#         print('Please enter a number')
#     else:
#         print('Thank You')
#         break


# 2.
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as error:
#         print(f'Please enter numbers {error}')

# print(sum(1, '2'))


# 3.
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter a number')
        break
    else:
        print('Thank You')
        break
    finally:
        print('Okay, we\'re done')
    print('Can you hear me?')
