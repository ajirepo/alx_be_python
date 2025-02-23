num=int(input("Enter the size of the pattern: "))
outer_count = 0
while outer_count < num:
  # Outer loop controls the number of times the inner loop runs
  inner_count = 0 
  for inner_count in range (num):
    # Inner loop repeats for each outer loop iteration
    print("*", end=" ")
    inner_count +=0
  print()  # Move to a new line after each outer loop iteration
  outer_count  +=1
