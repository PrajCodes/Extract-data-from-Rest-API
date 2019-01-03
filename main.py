import argparse
import json
import requests

#parsing command line arguments
parser = argparse.ArgumentParser(description='This script counts the most active days of the week in the past year of a github repository')
parser.add_argument('--weeks',type=int, help='Number of weeks into the past to be considered ')
parser.add_argument('--sort',type=str, help='Mention the way results are to be sorted ')
parser.add_argument('repo', type=str,help='Repository name')
args = parser.parse_args()

repoName=args.repo
weeksarg=args.weeks
sortarg=args.sort
#getting JSON information from the repository statistics API of github REST API to get commit activity of past year
commitStatsUrl = requests.get('https://api.github.com/repos/{}/stats/commit_activity'.format(repoName))
commitYearlyActivity=json.loads(commitStatsUrl.content)
#commitYearlyActivity is a list of dictionaries containing list of commit stats for each day per week 
numCommitsEachDay=[0,0,0,0,0,0,0]
if(weeksarg is None):
	numWeeks=len(commitYearlyActivity)
else:
	numWeeks= weeksarg

for i in range(numWeeks):
	currentWeek=commitYearlyActivity[i]
	for day in range(len(numCommitsEachDay)):
		numCommitsEachDay[day]=numCommitsEachDay[day]+currentWeek['days'][day]

if(sortarg is None or sortarg=="desc"):
	sortedIndices=sorted(range(len(numCommitsEachDay)),key=numCommitsEachDay.__getitem__, reverse=True)
elif(sortarg=="asc"):
	sortedIndices=sorted(range(len(numCommitsEachDay)),key=numCommitsEachDay.__getitem__)

daysOfWeek=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#average=int(max(numCommitsEachDay)/len(commitYearlyActivity))
#print(maxDay,average)
for si in sortedIndices:
	print(daysOfWeek[si],round(numCommitsEachDay[si]/numWeeks))

