# Define the number of rows for the pattern
num_rows = 5

# Upper half of the pattern
for i in range(1, num_rows + 1):
    print('*' * i)

# Lower half of the pattern
for i in range(num_rows - 1, 0, -1):
    print('*' * i)
