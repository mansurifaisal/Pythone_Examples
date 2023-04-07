# # problem 1 solution

# list_of_number = list(range(27))
# print(list_of_number)

# alphabets = " ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
# alphabet_list = alphabets.split(",")
# print(alphabet_list)

# alphabet_dict = dict(zip(list_of_number,alphabet_list))
# print(alphabet_dict)

# # problem 2 solution

# encrypted_message = ("ajsuydtbe", "", "wunjbfusnjrgut", "uhbhr", "oirun", "lpef", "", "vhejsibr", "ydtse", "qlvuusrntuos", "ijwlbutybhlsoaxh")

# string_lenght_list = []

# for message in encrypted_message:
#     print(len(message))

# # string_lenght_list.append(print(len(alphabet_dict)))

# decrypted_message = ""

# print(alphabet_dict.get(9))
# print(alphabet_dict.get(0))
# print(alphabet_dict.get(14))
# print(alphabet_dict.get(5))
# print(alphabet_dict.get(5))
# print(alphabet_dict.get(4))
# print(alphabet_dict.get(0))
# print(alphabet_dict.get(8))
# print(alphabet_dict.get(5))
# print(alphabet_dict.get(12))
# print(alphabet_dict.get(16))

# # problem 3 solution

# jumbled_word = ["hugdtck", "tsogbklesrawqcbjplu", "qkisrubskoaitbt", "nslaoetr", "oksinjioaendnjsdqwbh"]

# for jumbled in jumbled_word:
#     print(len(jumbled))

# chars_in_jumbled_state = []

# print(alphabet_dict.get(7))
# print(alphabet_dict.get(19))
# print(alphabet_dict.get(15))
# print(alphabet_dict.get(8))
# print(alphabet_dict.get(20))

# list = ['g', 's', 'o', 'h', 't']
# sorted_char_list = sorted(list)
# print(sorted_char_list)

# correct_word = "ghost"
# print(f'I saw a {correct_word} please help me soon')

# problem 4 solution

# perfect_number_candidate = int(input(''))
# sum1 = 0
# i = 1

# if perfect_number_candidate <= 0:
#     print('Invalid Number.')
# else:
#     while(i < perfect_number_candidate):
#         if perfect_number_candidate % i == 0:
#             sum1 = sum1 + i
#             i += + 1
#         else:
#             i+=1
#     if sum1 == perfect_number_candidate:
#         print(perfect_number_candidate, "is a perfect number")
#     else:
#         print(perfect_number_candidate, "is not a perfect number")

# # problem 5 solution

# movie_quote = "If you let my daughter go now, that'll be the end of it. I will not look for you, I will not pursue you. But if you don't, I will look for you, I will find you, and I will kill you."

# movie_quote_list = movie_quote.replace(',','').replace('.','')
# print(movie_quote_list)

# list_of_words = movie_quote_list.split(' ')
# print(list_of_words)

# for words in list_of_words:
#     if len(words) > 3:
#         print(words)

# unique_words = ["look, pursur, find, kill"]
# print(f'The unique word list is {unique_words}')