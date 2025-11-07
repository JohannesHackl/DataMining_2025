import pandas as pd

df = pd.read_csv("damin2025/lecture02/exercises/data/student_grades.csv")
print(df.shape)
rows, columns = df.shape

#----------------------------------------------------------------------
# Display the first few rows
print(df.head())

#----------------------------------------------------------------------
# calculate the average grade for each student
df['AverageGrade'] = df.iloc[:, 1:].mean(axis=1).round(1)
# print(df[['Student', 'AverageGrade']])
      
#----------------------------------------------------------------------
# handle missing data.

# print(df.isnull().sum())
'''     # number of missing values per column:
Student               0
Math                  0
Science               2
English               0
History               0
Geography             1
Art                   1
Physical Education    4
Music                 1
Biology               0
Chemistry             1
AverageGrade          0
'''

# fill with the average
# for i in range(1, df.columns.size):     # 11 columns
#     df.iloc[:,i] = df.iloc[:,i].fillna(df.iloc[:,i].mean())

# fill with 0s
df_filled = df.fillna(0)

#----------------------------------------------------------------------
# print only the students who scored above 85.
threshold = 85
subjects = df.columns.drop('Student')

print('\n')

for index, row in df.iterrows():
    student = row['Student']
    high_scores= []

    for subject in subjects:
        grade = row[subject]
        if pd.notna(grade) and grade > threshold:
            high_scores.append(f'{int(grade)} ({subject})')

    if high_scores:
        print(f'{student}: {', '.join(high_scores)}')

#----------------------------------------------------------------------
# print(df.head())
