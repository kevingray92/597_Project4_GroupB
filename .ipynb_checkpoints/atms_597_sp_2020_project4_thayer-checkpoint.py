import pandas as pd
import glob

path = '/content/drive/My Drive/Colab Notebooks/Project_4/GFSSfc/bufkit/' # CHANGE TO YOUR FILE PATH FOR THE UNTARRED FILES
all_files = glob.glob(path + "*.csv")
all_files.sort()

GFS_array = []

for i in np.arange(0,len(all_files)):

  filename = all_files[i].split(".")
  filename1 = filename[0].split('/')[-1]

  if int(filename1[0:4]) < 2020: ## Only using files with an initialization date before 2020-01-01

    if i == 0: ## Only appending column names for first file
      GFS_file_df = pd.read_csv(all_files[i], header=0)
      GFS_file_df = GFS_file_df.T # Transposing dataframe
      GFS_file_df = GFS_file_df.rename(index={'Unnamed: 0':'Date'}) # Changing first value within index column to 'Date'
      GFS_file_df = GFS_file_df.drop(GFS_file_df.columns[[0, 1, 2, 3, 5, 7, 8]], axis=1) # Retaining only Temp, Wind Speed, Precip columns
      GFS_file_df = GFS_file_df[[6,9,4]] # Re-arranging columns to the same order as the KCMI data
      GFS_array.append(GFS_file_df.iloc[:, 0:3]) # Only appending 06Z-06Z forecasts
    else: ## Only appending 06Z-06Z data after the first file
      GFS_file_df = pd.read_csv(all_files[i], header=0)
      GFS_file_df = GFS_file_df.T # Transposing dataframe
      GFS_file_df = GFS_file_df.drop(GFS_file_df.columns[[0, 1, 2, 3, 5, 7, 8]], axis=1) # Retaining only Temp, Wind Speed, Precip columns
      GFS_file_df = GFS_file_df[[6,9,4]] # Re-arranging columns to the same order as the KCMI data
      GFS_array.append(GFS_file_df.iloc[1:, 0:3]) # Only appending 06Z-06Z forecasts

GFS_Sfc_42hrFcst = pd.concat(GFS_array, axis=0)
GFS_Sfc_42hrFcst.to_csv('/content/drive/My Drive/Colab Notebooks/Project_4/GFSSfc/GFS_Sfc_42hrFcst_2010thru2019.csv')


