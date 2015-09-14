#GitIssues

**About**     
This is a tool I made to ease my nervous-tick of having to create Issues ONLY via GitHub's Issue page. Now, I can do this via the command line.

**Usage**     
After cloning the repo, type the following command:    
$pip install --editable .
Now, you can start executing commands.

Keep in mind that support for both Python 2 and 3 is tough. I'm trying to find ways to counter this, but currently, this is only runnable (successfully) when installed into a [virtualenv](http://click.pocoo.org/5/quickstart/#virtualenv). It can be executed for Python3 at the moment, but is buggy for Python2.

To list Issues in a repo, type the following and follow the prompts:    
      $gi list     

To post Issues, type the following
  $gi open --title TITLE MESSAGE 



**Tools**     
GitIssues was made with [Click](http://click.pocoo.org/5/), which is a nice Python package that aides in creating command-line interfaces.
