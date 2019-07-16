# Software will analyse a Big Data Set of Baseball players
# currently playing on the MLB.
import numpy as np
import matplotlib.pyplot as plt
import csv
with open("baseball_reference_2016_clean.csv", 'r') as f:
    baseball = list(csv.reader(f, delimiter=","))

stat_receipt = open("MoneyBall_Statistics_Recipt.txt", "w")

baseball = np.array(baseball[1:], dtype=np.str)

# IMPORTANT METHODS
# ------------------------------------------------
# DISPLAY DATA FUNCTIONS                         |
# ------------------------------------------------

# Displays Attendance
def display_average_attendance(teamName):
    attendanceSum = 0.0
    count = 0
    for i in range(len(baseball)):
        if(baseball[i][9] == teamName):
            attendanceSum = attendanceSum + float(baseball[i][1])
            count = count + 1
    stat_receipt.write(teamName + " had an attendance of " + str("%.2f" % round(attendanceSum/count,2)) + "\n")
    print(teamName + " had an attendance of " + str("%.2f" % round(attendanceSum/count,2)))


# Displays Home Team Hits
def display_average_team_hits(teamName):
    hitsSum = 0.0
    count = 0
    for i in range(len(baseball)):
        if(baseball[i][9] == teamName):
            hitsSum = hitsSum + float(baseball[i][11])
            count = count + 1
    stat_receipt.write(teamName + " had an average of " + str("%.2f" % round(hitsSum/count,2)) + " hits." + "\n")
    print(teamName + " had an average of " + str("%.2f" % round(hitsSum/count,2)) + " hits.")

# Displays Home Team Runs
def display_average_team_runs(teamName):
    runsSum = 0.0
    count = 0
    for i in range(len(baseball)):
        if(baseball[i][9] == teamName):
            runsSum = runsSum + float(baseball[i][12])
            count = count + 1
    stat_receipt.write(teamName + " had an average of " + str("%.2f" % round(runsSum/count,2)) + " runs." + "\n")
    print(teamName + " had an average of " + str("%.2f" % round(runsSum/count,2)) + " runs.")

# Display Season (W/L) Record
def display_win_loss_record(teamName):
    wins = 0
    loss = 0
    for i in range(len(baseball)):
        if(baseball[i][9] == teamName):
            if(baseball[i][25] == "Win"):
                wins = wins + 1
            elif(baseball[i][25] == "Loss"):
                loss = loss + 1
    stat_receipt.write(teamName + " record: (Wins: " + str(wins) + ", Loss: " + str(loss) + ")" + "\n")
    print(teamName + " record: (Wins: " + str(wins) + ", Loss: " + str(loss) + ")")


#------------------------------------------------------------
# GRAPH FUNCTIONS                                           |
# -----------------------------------------------------------

# Graph Attendance During Season
def graph_attendance(teamName):
    attendance = []
    game_day = []
    count = 1
    for i in range(len(baseball)):
        if(baseball[i][9] == teamName):
            attendance.append(float(baseball[i][1]))
            game_day.append(count)
            count = count + 1

    plt.plot(game_day, attendance)
    plt.ylabel('Attendance')
    plt.xlabel('Game Week')
    plt.title(teamName + " Home Attendance")
    plt.show()

# Graph Hits during each game
def graph_hits(teamName):
    hits = []
    game_day = []
    count = 1
    for i in range(len(baseball)):
        if(baseball[i][9] == teamName):
            hits.append(float(baseball[i][11]))
            game_day.append(count)
            count = count + 1

    plt.plot(game_day, hits)
    plt.ylabel('Hits')
    plt.xlabel('Game Week')
    plt.title(teamName + " Hits on Home Games")
    plt.show()

# Graph Runs during each game
def graph_runs(teamName):
    runs = []
    game_day = []
    count = 1
    for i in range(len(baseball)):
        if(baseball[i][9] == teamName):
            runs.append(float(baseball[i][12]))
            game_day.append(count)
            count = count + 1

    plt.plot(game_day, runs)
    plt.ylabel('Runs')
    plt.xlabel('Game Week')
    plt.title(teamName + " Runs on Home Games")
    plt.show()

#------------------------------------------------
# Printing MoneyBall Statisticall Receipt       |
#------------------------------------------------
def print_receipt(receipt):
    stat_receipt.write(receipt)

# Program
receipt = ""
answer = True
con = input("Welcome to MoneyBall, the Baseball Data Analytics Software!\n" +
      "This DA Software analyses MLB fixtures from the 2016 MLB season.\n\n" +
      "Press 1 to continue or 0 to quit.")
while(answer == True):
    if(con == str(1)):
        print("Instructions: \n" +
              "1) Select what data do you wish to analyse or graph.\n" +
              "2) Select the team that you want to analyse.\n" +
              "3) Press Enter. \n")
        sel = input("Select what to do: \n" +
              "0) Average Attendance.\t" + "4) Graph Attendance.\n" +
              "1) Average Team Hits. \t" + "5) Graph Team Hits. \n" +
              "2) Average Team Runs. \t" + "6) Graph Team Runs.\n" +
              "3) Home Wins / Home Loss\n")
        team = input("MLB TEAM: \n" +
                     "New York Yankees\tChicago Cubs\tLos Angeles Dodgers\tBoston Red Sox\tNew York Mets\n" +
                     "Toronto Blue Jays\tPhiladelphia Phillies\tSt. Louis Cardinals\tHouston Astros\tAtlanta Braves\n" +
                     "Minnesota Twins\tLos Angeles Angels\tSan Francisco Giants\tSeattle Mariners\tCleveland Indians\n" +
                     "Chicago White Sox\tSan Diego Padres\tCincinnati Reds\tTampa Bay Rays\tPittsburgh Pirates\n" +
                     "Detroit Tigers\tTexas Rangers\tArizona Diamondbacks\tWashington Nationals\tBaltimore Orioles\n" +
                     "Oakland Athletics\tMiami Marlins\tKansas City Royals\tColorado Rockies\tMilwaukee Brewers\n\n")
        print("Stat:")
        if(sel == str(0)):
            display_average_attendance(team)
        elif(sel == str(1)):
            display_average_team_hits(team)
        elif(sel == str(2)):
            display_average_team_runs(team)
        elif(sel == str(3)):
            display_win_loss_record(team)
        elif(sel == str(4)):
            graph_attendance(team)
        elif(sel == str(5)):
            graph_hits(team)
        elif(sel == str(6)):
            graph_runs(team)
        else:
            print("Enter a valid number")


        con = input("Do you wish to continue? 1 (yes) or 0 (no): ")
        if(con == str(0)):
            print_receipt(receipt)
    elif(con == str(0)):
        print("Thanks for using MoneyBall, Goodbye!")
        answer = False
    else:
        con = input("ERROR: wrong number! SELECT 1 OR 0!")
