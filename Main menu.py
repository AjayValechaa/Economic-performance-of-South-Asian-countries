##############################################################################
#                    Socio-Economic Indicators Portal                        #
#Team Members: Aamir Abbas, Ali Iftikhar, Premkumar Loganathan, Ajay Valecha #
##############################################################################

# Importing all the packages and functions needed 

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from pandas.io.json import json_normalize
from urllib.request import urlretrieve as retrieve
import matplotlib.pyplot as plt
import seaborn as sns
from Plots import indicator_plot, compare_plot, analyze_plot
from Country_Profile import country_profile1, country_profile2
from Single_Country import single_country
from Multiple_Countries import multiple_countries
from Select_Indicator import select_indicator
from Single_Indicator_df import single_indicator_df
from Two_Indicator_df import two_indicator_df
from WHO_Data_csv import WHO_data


# In[7]:


#function name is manu()
# it does not have any paramter
# it prompts the user to enter options from 1 to 3 and 0 to exit 
# returns the option entered by the user 
def menu():
    #printing the welcome message 
    print("""             ######################################################################################
          
             ############       Welcome to Socio-Economic Indicators Portal     ###################
             
             ######################################################################################""")
    # Prompting the usre for input 
    User_input = int(input("""\t\t\t What would you like to know today?
            1. Know about a South East Asian country
            2. Compare performance of South East Asian countries on different indicators
            3. Analyze Social and Economic indicators for a South East Asian country
            0. To exit \n
            Please enter your choice: """))
    return(User_input)






#The main function takes no parameters 
#It prompts the user to select between a menu of options 
# The options are
#01. Know about a country (Gives country profile)
#02. Compare performance of different countries on an indicator (two or more countries)
#03. To find the correlation of any two indicators within the country 
#when moving in different options the guidelines will be provided on the go for each option 

def main():
    
    
    User_input_0 = 1
    #This is the main while loop which runs the prompt to the user 
    while User_input_0 != 0: 
        User_input_0 = menu()
        if User_input_0 == 1:
            User_input_1a = 1
            while User_input_1a != 0:
                User_input_1a = single_country()
                #Get country profile 1 and 2 and show it  
                if len(User_input_1a) > 0:
                    country_profile1(User_input_1a[1])
                    country_profile2(User_input_1a[0])
                    User_input_1b = 1
                    while User_input_1b != 0:
                        #selecting the indicator and plot the indicator 
                        User_input_1b,label = select_indicator()
                        df_country =  single_indicator_df(User_input_1a[0], User_input_1b)
                        indicator_plot(User_input_1a[1],label, df_country)
                        User_input_1c = int(input("To check another indicator for the same country ("+ ''.join(User_input_1a[1]) +") Enter 1. To check another country, Enter 2. To exit to main menu, Enter 3. To exit, Enter 0: "))
                        if User_input_1c == 2:
                            User_input_1b = 0
                        elif User_input_1c == 3:
                            User_input_1b = 0
                            User_input_1a = 0
                        elif User_input_1c == 0:
                            User_input_1b = 0
                            User_input_1a = 0
                            User_input_0 = 0
                else:
                    User_input_1a = 0
        # Incase user enters 2 in the main menu             
    
        elif User_input_0 == 2:
            User_input_2a = 1
            # Get different countries and plot their indicators 
            # Show a plot of the indicators comparison that are specified 
            while User_input_2a != 0:
                
                User_input_2a = multiple_countries()
                User_input_2b = 1
                while User_input_2b != 0:
                    User_input_2b,label = select_indicator()
                    df_country =  single_indicator_df(User_input_2a[0], User_input_2b)
                    compare_plot(User_input_2a[1],label,df_country)
                    User_input_2c = int(input("To compare " + ', '.join(User_input_2a[1]) + """ for another indicator Enter 1,
                    To compare different countries, Enter 2
                    To exit to main menu, Enter 3
                    To exit, Enter 0: """))
                    if User_input_2c == 2:
                        User_input_2b = 0
                    elif User_input_2c == 3:
                        User_input_2b = 0
                        User_input_2a = 0
                    elif User_input_2c == 0:
                        User_input_2b = 0
                        User_input_2a = 0
                        User_input_0 = 0
        # Select a country 
        # Identify two indicators 
        # Plot the correlations between the two 
        elif User_input_0 == 3:
            User_input_3a = 1
            while User_input_3a != 0:
                User_input_3a = single_country()
                User_input_3b = 1
                while User_input_3b != 0:
                    User_input_3b,label1 = select_indicator()
                    df_indicator1 =  single_indicator_df(User_input_3a[0], User_input_3b)
                    User_input_3c,label2 = select_indicator()
                    if User_input_3b == User_input_3c:
                        while User_input_3b == User_input_3c:
                            print('\n Error: Select a different indicator number\n')
                            User_input_3c,label2 = select_indicator()
                    label_list = [label1, label2]
                    df_indicator2 =  single_indicator_df(User_input_3a[0], User_input_3c)
                    df_list = [df_indicator1,df_indicator2]
                    analyze_plot(User_input_3a[1],[1,2],label_list,df_list)
                    User_input_3d = int(input("To analyze correlation for different indicators for " + ''.join(User_input_3a[1]) + """ Enter 1,
                    To analyze different countries, Enter 2
                    To exit to main menu, Enter 3
                    To exit, Enter 0: """))
                    if User_input_3d == 2:
                        User_input_3b = 0
                    elif User_input_3d == 3:
                        User_input_3a = 0
                        User_input_3b = 0
                    elif User_input_3d == 0:
                        User_input_3b = 0
                        User_input_3a = 0
                        User_input_0 = 0
        else:
            print("""You entered incorrect input!
            Please enter correct input or enter 0 to exit""")
                            
            

print("Thank you for visiting! Have a good day")    

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:




