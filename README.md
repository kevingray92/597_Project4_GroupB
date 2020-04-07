# 597_Project4_GroupB
## ATMS 597: Weather and Climate Data Science
### Project 4 Group B

Group Members: David Lafferty, Kevin Gray, Jeff Thayer

This program uses two regression techniques (multiple linear and random forest) found in the sklearn package and two datasets (KCMI observations and GFS model forecasts) to predict daily maximum temperature, minimum temperature, maximum wind speed, and total accumulated precipitation from 06Z-06Z over the period 2010-2019. Data from 2010-2018 is used for training and 2019 is used for validation (i.e. testing). The accuracy of each regression technique is determined by the root mean squared error for each predicted variable.

KCMI (Champaign, Illinois) daily extreme observations used in this program are for the period 06Z-06Z, while hourly observations are only used from 12Z-23Z the day prior to the 06Z-06Z predicted period. Of note, the daily accumulated precipitation lacks sufficient temporal coverage over 2010-2019, and thus the hourly precipitation resampled daily (i.e. accumulated over a day) is used in its place. Additional useful variables (e.g. pressure, cloud cover, dewpoint, geopotential height, etc.) from Global Forecast System (GFS) 3-hourly surface and profile model data valid for 06Z-06Z and initialized at 12Z the previous day are also used for training and validation. 

