# NEISA-rankings

How to use:  
Create 2 google sheets, following this structure:  

1. A sheet with all the schools in NEISA with the header "Schools" at the top.  
Follow this model: https://docs.google.com/spreadsheets/d/e/2PACX-1vQfU-xYwtTc9nlW_tpsEmk-TMlUqsvzLooC8m3tcFnS7ig3lvWkA_b_2BxzUNGik8zq6IV-Lg9BwGSV/pub?output=csv  

2. A sheet with each regatta and the type of that regatta. The type is denoted using the same structure we have used in the past. Follow this model exactly: https://docs.google.com/spreadsheets/d/e/2PACX-1vQfeyC1LeMtdi0qIz-GWxke3jPQ1jJzp72YNi_I9YXF1f73HXUBRTG7AqePHI_L5X54HVwAofxueTiO/pub?output=csv  

Note: The google sheets you should use is the link you get when going to File > Publish to Web. Change the Web Page setting to CSV using the dropdown. You should get a link from doing this.

In the Runner.py file, paste in the two links and specify two CSV files to output the results to. Put each of these between quotes (like the way it is now). For the way it is currently set up, the results will be contained in the rankings.csv file and the component scores.csv file. When everything is set, run the Runner.py script.

Call RankCalculator.CalculateScoreTable(maximumNumberOfTeams, minimumNumberOfTeams, "regattaType") in in order to get the scoring table that the code is using. It will print out to your console. For example, calling RankCalculator.CalculateScoreTable(18, 18, "A"), will print out:   
for teams: 18  
8.5  
8.0  
7.5  
7.0  
6.5  
6.0  
5.5  
5.0  
4.5   
4.0  
3.5   
3.0  
2.5   
2.0  
1.5   
1.0   
0.5   
0.0   
If there were more teams (ex: RankCalculator.CalculateScoreTable(18, 16, "A")) it would print out the same thing but for 18, 17, and 16 teams.

For Mike to run the python file:

NOTE: Case matters in the following commands.

Open Terminal

Type 'neisa'

Type 'python3 Runner.py'
