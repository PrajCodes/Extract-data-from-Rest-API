# Extract-data-from-Rest-API
A python script to extract the required data about a particular Github Repo from Github REST API.  readme file has the description of instructions and dependencies.

The python script main.py displays the average number of git commits made on each day of the week
considering the report from github commit status from the past year i.e past 52 weeks. 

The input to main.py is expected to be a string containing username/repositoryname, i.e the link to repository.
eg : kubernetes/kubernetes
The output displays the day of the week followed by average commits made on that day calculated for the past year.

The script also allows optional command line arguments --week and --sort.
--week limits  the number of weeks into the past to be considered and --sort allows to sort the result in ascending or descending order. 

In order to run the script: argparse, json and requests are the 3 dependent libraries to be installed. 

The version requirements of the above libraries used to test are:
requests==2.18.4
argparse==1.1
json==2.0.9
 

Assumptions made  are: Input will contain a valid url to a github repository and will contain both username and repo name, 
number of weeks specified will not be greater than 52, value for --sort argument will be either None, asc or desc. 

