import pandas as pd
import os




output_dir = "selected_participants"
os.makedirs(output_dir, exist_ok=True)

abide_input_file = "ABIDE_phenotypic_NYU.csv"
adhd200_input_file = "adhd200_phenotypics.tsv"




abide_df = pd.read_csv(abide_input_file)
adhd200_df = pd.read_csv(adhd200_input_file, sep='\t')

# Define your conditions
# Example: Selecting rows where AGE_AT_SCAN is greater than 18 and SEX is 'Male'
filtered_abide_df = abide_df[
    (5 < abide_df['AGE_AT_SCAN']) & (abide_df['AGE_AT_SCAN'] < 13) &
    (80 < abide_df['FIQ']) & (abide_df['FIQ'] < 140) &
    (80 < abide_df['VIQ']) & (abide_df['VIQ'] < 140) &
    (80 < abide_df['PIQ']) & (abide_df['PIQ'] < 140) # Example condition
]

filtered_adhd200_df = adhd200_df[
    (5 < adhd200_df['Age']) & (adhd200_df['Age'] < 13) &
    (80 < adhd200_df['Full4 IQ']) & (adhd200_df['Full4 IQ'] < 140) &
    (80 < adhd200_df['Verbal IQ']) & (adhd200_df['Verbal IQ'] < 140) &
    (80 < adhd200_df['Performance IQ']) & (adhd200_df['Performance IQ'] < 140) # Example condition
]


#print(filtered_adhd200_df.columns.tolist())

output_file1_1 = os.path.join(output_dir, "ABIDE_pure_ASD_phenotypic_NYU.csv")
output_file1_2 = os.path.join(output_dir,"ADHD200_pure_ADHD_phenotypic_NYU.csv")

pure_ASD_df = filtered_abide_df[
    (filtered_abide_df['DX_GROUP'] == 1) &
    (
            (filtered_abide_df['COMORBIDITY'].str.strip() == '') | (filtered_abide_df['COMORBIDITY'].isna())
    )
]
filtered_adhd200_df = filtered_adhd200_df.copy()
filtered_adhd200_df['DX'] = pd.to_numeric(filtered_adhd200_df['DX'], errors='coerce')

pure_ADHD_df = filtered_adhd200_df[
    (filtered_adhd200_df['DX'] == 1) | (filtered_adhd200_df['DX'] == 2) | (filtered_adhd200_df['DX'] == 3) &
    (
            (filtered_adhd200_df['Secondary Dx'].str.strip() == '') | (filtered_adhd200_df['Secondary Dx'].isna())
    )
]


pure_ASD_df.to_csv(output_file1_1, index=False)
pure_ADHD_df.to_csv(output_file1_2, index=False)



output_file2_1 = os.path.join(output_dir,"ABIDE_ASD_ADHD_Comorbid_phenotypic_NYU.csv")

ASD_ADHD_df = filtered_abide_df[
    (filtered_abide_df['DX_GROUP'] == 1) &
    (filtered_abide_df['COMORBIDITY'].str.contains('ADHD', na=False, case=False))
]

ASD_ADHD_df.to_csv(output_file2_1, index=False)


output_file3_1 = os.path.join(output_dir,"ABIDE_TD_phenotypic_NYU.csv")
output_file3_2 = os.path.join(output_dir,"ADHD200_TD_phenotypic_NYU.csv")

td_abide_df = filtered_abide_df[
    (filtered_abide_df['DX_GROUP'] == 2)
]

td_adhd_df = filtered_adhd200_df[
    (filtered_adhd200_df['DX'] == 0)
]

td_abide_df.to_csv(output_file3_1, index=False)
td_adhd_df.to_csv(output_file3_2, index=False)