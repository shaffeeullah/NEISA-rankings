# NEISA-rankings

## How to use:  
Create 2 google sheets, following this structure:  

1. A sheet with all the schools in NEISA with the header "Schools" at the top.  
Follow this model: https://docs.google.com/spreadsheets/d/e/2PACX-1vQfU-xYwtTc9nlW_tpsEmk-TMlUqsvzLooC8m3tcFnS7ig3lvWkA_b_2BxzUNGik8zq6IV-Lg9BwGSV/pub?output=csv  

2. A sheet with each regatta and the type of that regatta. The type is denoted using the same structure we have used in the past. Follow this model exactly: https://docs.google.com/spreadsheets/d/e/2PACX-1vQfeyC1LeMtdi0qIz-GWxke3jPQ1jJzp72YNi_I9YXF1f73HXUBRTG7AqePHI_L5X54HVwAofxueTiO/pub?output=csv  

Note: The google sheets you should use is the link you get when going to File > Publish to Web. Change the Web Page setting to CSV using the dropdown. You should get a link from doing this.

In the Runner.py file, paste in the two links and specify two CSV files to output the results to. Put each of these between quotes (like the way it is now). For the way it is currently set up, the results will be contained in the `rankings.csv` file and the `component_scores.csv file`. When everything is set, run the Runner.py script (`python3 Runner.py` from the `neisa` directory).

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

To call this function, type the following commands into your terminal
1. `python3`
2. `import RankCalculator`
3. `RankCalculator.CalculateScoreTable(9, 9, "C")` (or whatever you want the parameters to be)
Type `exit()` to get back to the main terminal.

## For Mike to Run the Python File:   
NOTE: Capitals matter in the following commands. Also, the `neisa` command will only work on your personal laptop. If you are not on your laptop or anyone follows the below instructions on a different machine, run `cd ~/Desktop/NEISA-rankings-master` *instead* of `neisa`.  

0. Open Terminal  
1. Type `neisa`   
2. Type `python3 Runner.py`  
3. Files will appear in Finder under Desktop/NEISA-rankings-master

## For Mike to Get Updated Code:

0. Save the links that are at the top of Runner.py somewhere (e.g. Notes)
1. Come to this page! Congrats.  
2. Hit the green *Clone or download* button in the upper right corner of the page.
3. Hit *Download ZIP*
4. The zip should download. Double click the download to unzip it into a folder. (Finder should open). Drag that folder into your Desktop. If it asks you to replace the existing one, say yes.
5. **VERY IMPORTANT**: Make sure the folder is called **NEISA-rankings-master**. Make sure there's no (1) or (2) at the end.
6. Update the links at the top of Runner.py if they are not correct.
7.  See above to run it!
