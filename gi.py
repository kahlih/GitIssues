import click

username = ''
repo = ''

@click.command()
@click.option('--config', nargs=2,type=str, help="This command lists the issues in your repo")
def cli(config):
	username = config[0]
	repo = config[1]
	target = open(".config", 'w').close()	
	target = open(".config", 'w')
	target.write(username)
	target.write("\n")
	target.write(repo)
	target.write("\n")	
	print("Hello!", username, repo)
	print("username", username)
	print("repo ", repo)

