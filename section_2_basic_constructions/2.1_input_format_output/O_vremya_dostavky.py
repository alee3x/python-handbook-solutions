starting_hours = int(input())
starting_minutes = int(input())
wait_all= int(input())

wait_hours = wait_all // 60
wait_minutes = (wait_all % 60) + starting_minutes

final_hours = (starting_hours + wait_hours + (wait_minutes // 60)) % 24
final_minutes = wait_minutes % 60

print(f"{final_hours:0>2}:{final_minutes:0>2}")
