import click
import requests
import json
import getpass

username = 'kahlih'
repo = 'Competitive-Programmming'

url_head = "https://api.github.com/repos/"

@click.group()
def cli():
	pass

@cli.command()
def list():
	url = url_head + username + "/" + repo + "/issues"
	response = requests.get("https://api.github.com/repos/kahlih/Competitive-Programming/issues")	
	d=json.loads(response.content.decode('utf8'))
	#d = d[0]
	click.echo(click.style("Issues for Repo: Competitive-Programming", fg="green", reverse=True))	
	for i in d:
		s = str("#" + str(i["number"]) + ": " + i["title"])
		click.echo(click.style(s, fg="blue"))

@cli.command()
@click.option("--t", default="Another Issue", help="none") 
@click.argument('message')
def open(t,message):
	username = input('Github username: ')
	password = getpass.getpass('Github password: ')	
	
	d = {}
	d["title"]=t
	d["body"]=message
	
	this_url = url_head + username + "/" + repo + "/issues"
	res = requests.post(
        	url="https://api.github.com/repos/kahlih/Competitive-Programming/issues",
        	auth = (username, password),
        	data = json.dumps(d),
        )
	if(res.status_code == 201):
		click.echo(click.style("Issue created", fg="cyan")) 
	else:
		print(res.status_code, res.reason)


