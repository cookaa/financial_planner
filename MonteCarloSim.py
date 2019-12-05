import random
import matplotlib.pyplot as plt
import numpy as np
#Create function for simulating die roll 
#The die can take values from 1 to 100. If the number is between 1 #and 51, the house wins. 
#If the number is between 52 and 100, the player wins.

def rolldice():

    dice = random.randint(1,100)
    
    if dice <=51:
        return False
    elif dice >51 & dice <=100:
        return True

#Define a function for the play which takes 3 arguments :
# 1. total_funds = total money in hand the player is starting with
# 2. wager_amount = the betting amount each time the player plays
# 3. total_plays = the number of times the player bets on this game
def play(total_funds, wager_amount, total_plays):
    
    #Create empty lists for :
    # 1.Play_number and 
    # 2.Funds available
    # 3.Final Fund
    Play_num = []
    Funds = []
    #TODO 
    Funds_mean = []

#Start with play number 1
    play = 1
#If number of plays is less than the max number of plays we have set
    while play < total_plays:
        #If we win
        if rolldice():
            #Add the money to our funds
            total_funds = total_funds + wager_amount
            #Append the play number
            Play_num.append(play)
            #Append the new fund amount
            Funds.append(total_funds)

            #TODO Append the new fund amount
            # avg_funds = total_funds - wager_amount
            # Funds_mean.append(avg_funds)
            #TODO Calculate the simple average of the data
            Funds_mean = [np.mean(Funds)]*len(Play_num)

        #If the house wins
        else:
            #Add the money to our funds
            total_funds = total_funds - wager_amount 
            #Append the play number
            Play_num.append(play)
            #Append the new fund amount
            Funds.append(total_funds)

            #TODO Append the new fund amount
            # avg_funds = total_funds - wager_amount
            # Funds_mean.append(avg_funds)
            
        #
            #TODO Calculate the simple average of the data
            Funds_mean = [np.mean(Funds)]*len(Play_num)

        #Increase the play number by 1
        play = play + 1

        if (play == total_plays-1):
            #TODO Plot the average line Needs to run one time
            # mean_line = plt.plot(Play_num,Funds_mean, label='Mean', linestyle='--')
            # plt.plot(Play_num,Funds_mean,linewidth=3.0,color='blue', marker='x')
             i = 1
#END OF PLAY()

    #Line plot of funds over time
    plt.plot(Play_num,Funds,linestyle='dashed')
    Final_funds.append(Funds[-1])
    return(Final_funds)

#Call the function to simulate the plays and calculate the remaining #funds of the player after all the bets
#Intialize the scenario number to 1
x=1
#Create a list for calculating final funds
Final_funds= []

while x<=100:
    ending_fund = play(10000,100,100)
    x = x+1


# Make a legend
legend = plt.legend(loc='upper right')

#Plotting 
plt.ylabel('Player Money in $')
plt.xlabel('Number of bets')
plt.show()


#Print the money the player ends with
print("The player starts the game with $10,000 and ends with $" + str(sum(ending_fund)/len(ending_fund)))
