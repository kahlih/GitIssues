import click
import requests
import json
import getpass
import sys

url_head = "https://api.github.com/repos/"

def print_version(ctx, param, value):
	if not value or ctx.resilient_parsing:
		return
	click.echo('Version 1.0')
	ctx.exit()

@click.group()
@click.option('--version', is_flag=True, callback=print_version,expose_value=False, is_eager=True)
def cli():
	pass

@cli.command()
def list():
	if sys.version_info[0] == 3:
		repo = input('Github Repo: ')
		username = input('Github username: ')
		password = getpass.getpass('Github password: ')	
	# Catches issue if Python3 is not being used
	# Need to patch this better so user is not prompted twice
	else:
		repo = raw_input('Github Repo: ')
		username = raw_input('Github username: ')
		password = getpass.getpass('Github password: ')
	
	turl = "" + url_head + username + "/" + repo + "/issues"
	
	response = requests.get(url=turl,auth=(username, password))	
	d=json.loads(response.content.decode('utf8'))
	click.echo(click.style("Issues for Repo: " + repo, fg="green", reverse=True))	
	for i in d:
		s = str("#" + str(i["number"]) + ": " + i["title"])
		click.echo(click.style(s, fg="blue"))

@cli.command()
@click.option("--title", default="Another Issue", help="none") 
@click.argument('message')
@click.argument('assignee', required=False, type=str)
@click.argument('milestone', required=False, type=int)
@click.argument('labels', required=False, type=str)
def open(title,message, assignee, milestone, labels):
	try:
		repo = input('Github Repo: ')
		username = input('Github username: ')
		password = getpass.getpass('Github password: ')	
	except NameError:
		print("Sorry, My Fault. Try Again")
		repo = raw_input('Github Repo: ')
		username = raw_input('Github username: ')
		password = getpass.getpass('Github password: ')
	d = {}
	d["title"]=title
	d["body"]=message
	if (assignee):
		d["assignee"]=assignee
	if (milestone):
		d["milestone"]=milestone
	if (labels):
		l = [labels]
		d["labels"]=l
	
	this_url = url_head + username + "/" + repo + "/issues"
	res = requests.post(
        	url=this_url,
        	auth = (username, password),
        	data = json.dumps(d),
        )
	if(res.status_code == 201):
		click.echo(click.style("Issue created", fg="cyan")) 
	else:
		print(res.status_code, res.reason)

@cli.command()
@click.option('--num', prompt="What is the number of the Issue you would like to edit")
@click.argument('title', required=False, type=str)
@click.argument('message', required=False, type=str)
@click.argument('assignee', required=False, type=str)
@click.argument('milestone', required=False, type=int)
@click.argument('labels', required=False, type=str)
def edit(num,title,message,assignee,milestone,labels):
	try:
		repo = input('Github Repo: ')
		username = input('Github username: ')
		password = getpass.getpass('Github password: ')	
	except NameError:
		print("Sorry, My Fault. Try Again")
		repo = raw_input('Github Repo: ')
		username = raw_input('Github username: ')
		password = getpass.getpass('Github password: ')

	this_url = url_head + username + "/" + repo + "/issues/" + num
	
	d={}
	if (title):
		d["title"]=title
	if (message):
		d["body"]=message
	if (assignee):
		d["assignee"]=assignee
	if (milestone):
		d["milestone"]=milestone
	if (labels):
		d["labels"]=labels

	res = requests.patch(
		url=this_url,
		auth = (username, password),
		data = json.dumps(d),
	)

	if(res.status_code == 200):
		click.echo(click.style("Issue Updated", fg="red"))
	else:
		print(res.status_code, res.reason)

@cli.command()
@click.argument('file')
def load(file):
	pass
