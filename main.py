# Name: OWOSENI ABIGAIL YEMISI
# Matric No: 24/15121
# Course Code: CUL-CYB 371
# Assignment: Fictional Student Dataset

import pandas as pd

# Creating a fictional student dataset
# All students are in 200 level
# Departments: Computer Science and Mass communication 

data = {
    "Student_Name": [
        "Tope Alabi",
        "Justin Okoro",
        "Anna Hathaway",
        "Michael Forge",
        "Angela Joseph",
        "Tony Gambe"
    ],
    "Student_ID_Matric_No": [
        "25/14212",
        "25/16215",
        "25/15131",
        "25/14211",
        "25/13242",
        "25/15244"
    ],
    "Department": [
        "Computer Science",
        "Mass Communication",
        "Mass Communication",
        "Computer Science",
        "Computer Science",
        "Mass Communication"
    ],
    "Level": [
        200,
        200,
        200,
        200,
        200,
        200
    ],
    "Attendance_Percentage": [
        92,
        78,
        88,
        65,
        95,
        71
    ],
    "Average_Examination_Score": [
        76,
        62,
        81,
        54,
        87,
        68
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)

# Save as CSV file
df.to_csv("fictional_student_dataset.csv", index=False)
print("\nDataset saved successfully as fictional_student_dataset.csv")
