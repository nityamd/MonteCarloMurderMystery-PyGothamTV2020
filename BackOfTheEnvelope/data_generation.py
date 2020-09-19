import pandas as pd

suspect_names = ['Viscountess Bae Zhun',  'Major Viktor Ljutenitsa', 'Ms Ingrid Hepburn',
                 'Lord Bryce Bloomington', 'Barrister Shannon Von Twist', 'Nurse Eliza Dill',
                 'Lady Barbara Bloomington', 'Mr. Miles Murdoch', 'Mr. Stan Hamilton','Python']


df = pd.DataFrame({suspects: suspect_names})
df['alibi'] = [0,0,1,0,0,1,1,1,0,1]
df['archery'] = [1,1,1,1,1,1,0,0,0,0]
df['inheritance'] = [1,0,0,0,0,0,0,0,1,0]
df['suspicion'] = [0,1,1,1,1,1,0,0,1,0]
df['animosity'] = [1,0,0,1,0,0,0,1,1,0]
df.to_csv('1_Watson_Interviews.csv', index = False)
