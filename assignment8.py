# # problem 1 solution:

# house_area_price_dict = {1056 : 39, 2600 : 120 , 1520 : 95, 1200 : 50, 2700 : 200, 1100 : 40}

# house_area = [1056, 2600, 1520, 1200, 2700, 1100]

# # for area in house_area:
# #     predicted_house_price = 0.05 * area + 10
# #     print(predicted_house_price)

# predicted_house_price = [0.05 * area + 10 for area in house_area]
# print(predicted_house_price)

# actual_house_price = [39, 120, 95, 50, 200]

# two_price_list = list(zip(actual_house_price,predicted_house_price))
# print(two_price_list)

# square_list = [(price_1**2,price_2**2) for price_1 in actual_house_price for price_2 in predicted_house_price]
# print(square_list)

# # problem 2 solution:

# x = [3, 9, 10, -4, -2, 1, 0, 4, 5, 7]

# import math

# sigmoid_x = [1 / (1 + math.exp(-x)) for x in x]
# print(sigmoid_x)

# boolean_value = [x > 0 and x < 1 for x in sigmoid_x]
# print(boolean_value)

# greater = [x for x in sigmoid_x if x > 0.5]
# print(greater)

# # problem 3 solution: 

# my_sentence = "I have been walking and running and dancing and smiling and laughing all my life, yet it all seems pointless."

# all_word_in_sentence = [sentence for sentence in my_sentence.split() if sentence.endswith('ing')]
# print(all_word_in_sentence)

# problem 4 solution:

sentence = 'Hello, good morning folks! Today we will announce the half yearly performance results of the company. Due to the ongoing COVID-19 pandemic, our profits have declined by 60% as compared to the last year'
print(sentence)

stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", 
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
              "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
              "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
              "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
              "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", 
              "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
              "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
              "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
              "don", "should", "now"}

custom_stop_words = ["hello","good","morning","half","year"]
updated_stop_words = list(stop_words)
stop_words_add = (updated_stop_words.extend(custom_stop_words))
print(stop_words_add)

sorted_stop_words = sorted(updated_stop_words)
print(sorted_stop_words)

word_in_sentence = [str(sentence)]
print(word_in_sentence)

removed_words = [word for word in custom_stop_words if word not in stop_words]
print(removed_words)

final_sentence = (" ").join([word for word in sentence.split(" ") if word not in sorted_stop_words])
print(final_sentence)
