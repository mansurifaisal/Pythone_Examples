# Assignment 9

# problem 1 solution:

def get_excel_column_number(column_name):

    result = 0
    column_number = 0
    for name in reversed(column_name):
        column_number += (ord(name) - ord('A') + 1) * (26 ** result)
        result += 1
    return column_number
print(get_excel_column_number(input()))
print(get_excel_column_number('BD'))
print(get_excel_column_number('ALQ'))

# problem 2 solution:

actual_labels = ['Cat','Dog','Cat','Cat','Dog','Cat','Dog','Cat','Cat','Cat','Dog','Dog','Cat','Cat','Cat','Dog','Dog','Dog','Cat','Dog']
predicted_labels = ['Cat','Dog','Cat','Cat','Dog','Cat','Dog','Cat','Dog','Dog','Dog','Dog','Cat','Cat','Cat','Dog','Dog','Dog','Cat','Cat']

print(len(actual_labels))
print(len(predicted_labels))

def calculate_accuracy (actual, predicted):
    '''This function calculate the accuracy of given labels'''
    sum(1 for actual,predicted in zip(actual_labels,predicted_labels) if actual == predicted) / len(actual_labels)
    return (actual, predicted)

accuracy = (calculate_accuracy('Cat', 'Dog'))
accuracy = sum(1 for actual,predicted in zip(actual_labels,predicted_labels) if actual == predicted) / len(actual_labels)
print(accuracy)

# problem 3 solution:

actual_labels = ['Cat','Dog','Cat','Cat','Dog','Cat','Dog','Cat','Cat','Cat','Dog','Dog','Cat','Cat','Cat','Dog','Dog','Dog','Cat','Dog']
predicted_labels = ['Cat','Dog','Cat','Cat','Dog','Cat','Dog','Cat','Dog','Dog','Dog','Dog','Cat','Cat','Cat','Dog','Dog','Dog','Cat','Cat']
lable = 'Dog'

def precision_recall(actual, predicted, lable):
    TP = sum(1 for actual, predicted in zip(actual_labels, predicted_labels) if actual == lable and predicted == lable)
    FP = sum(1 for actual, predicted in zip(actual_labels, predicted_labels) if actual != lable and predicted == lable)
    FN = sum(1 for actual, predicted in zip(actual_labels, predicted_labels) if actual == lable and predicted != lable)

    precision = TP/(TP + FP) if TP + FP > 0 else 0
    recall = TP/(TP + FN) if TP + FN > 0 else 0

    return precision, recall

precision_recall_lable = precision_recall(actual_labels, predicted_labels, lable)
print(f'Precision and Recall is: {precision_recall_lable}')

# problem 4 solution:

marvel_quote = "The world has changed and none of us can go back. All we can do is our best, and sometimes the best that we can do is to start over."

def fixed_length_word_count(sentence, length):
    length = 0
    count = sentence.replace('.','').replace(',','') 
    print(count)
    length = len(sentence.split(' '))
    print(f'The length of the input is: {length}')

fixed_length_word_count(marvel_quote, 0)
