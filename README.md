# NEISA-rankings

How to use:  
Create 2 google sheets, following this structure:  

1. A sheet with all the schools in NEISA with the header "Schools" at the top.  
Follow this model: https://docs.google.com/spreadsheets/d/e/2PACX-1vQfU-xYwtTc9nlW_tpsEmk-TMlUqsvzLooC8m3tcFnS7ig3lvWkA_b_2BxzUNGik8zq6IV-Lg9BwGSV/pub?output=csv  

2. A sheet with each regatta and the type of that regatta. The type is denoted using the same   
structure we have used in the past. Follow this model exactly: https://docs.google.com/spreadsheets/d/e/2PACX-1vQfeyC1LeMtdi0qIz-GWxke3jPQ1jJzp72YNi_I9YXF1f73HXUBRTG7AqePHI_L5X54HVwAofxueTiO/pub?output=csv

Call RankCalculator.calculateRanks(regattaLink, schoolslink)  
