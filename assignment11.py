# Assignment 6
# problem 1 solution
aravali = {"Dhoni": 25, "Virat": 31, "Pollard": 11, "Rohit": 0, "Maxwell": 12, "Sachin": 59, "Sehwag": 12}
print(list(aravali.keys()))

#problem 2 solution
total_runs = 195
player_runs = 150
Rohit_runs = (total_runs - player_runs)
print(Rohit_runs)

aravali.update({"Rohit": 45})
print(aravali)

#problem 3 solution
second_hightest = (print("The second hightes scored", aravali.get("Rohit")))

#problem 4 solution
run_set = (list(aravali.values()))
print(run_set)
unique_run = list(set(run_set))
print(unique_run)

#problem 5 solution
fixed = ['Hardik', 'Dravid', 'Smith', 'Jadeja', 'Yuvraj', 'Harbhajan']
mutable = ['Vijay', 'Lasith', 'Sushant', 'Rajeev', 'Amrit']
both = [fixed] + [mutable]
print(list(both))

#problem 6 solution
fixed[1] = 'Vijay'
print(fixed)
mutable[0] = 'Dravid'
print(mutable)

#problem 8 solution
runrate = (total_runs / 20)
print(runrate)

#problem 9 solution
message = "skdlfjnvuerhw qefnnaosfu qrhviudhfv wuirhv adknlkxjcier vafuvhkajn iuvhsf vasuif KJSHFKJ aeuihvasf akjfhiufe"

total_ball = list(range(120))
print(total_ball)

all_ball = list(zip(message, total_ball))
print(all_ball)

first_no_ball = all_ball.pop(29)
print(first_no_ball)

last_no_ball = all_ball.pop(103)
print(last_no_ball)

#problem 10 solution
B_run = int(input())

if B_run < 50:
    print("Smith will play")
elif B_run <= 100:
     print("Sir Jadeja will go")
else:
     print("Hardik will play")