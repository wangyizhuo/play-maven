import sys,os,inspect, shutil

COMMANDS = ['mvn:install', 'mvn:init', 'mvn:update', 'mvn:up', 'mvn:refresh', 'mvn:re', 'mvn:src', 'mvn:sources', 'mvn:play-dependency-sources', 'mvn:play-src']

def execute(**kargs):
	play_command = kargs.get("command")
	app = kargs.get("app")
	print app
	application_path = app.path
	if play_command == "mvn:install":
		module_dir = inspect.getfile(inspect.currentframe()).replace("commands.py","")
		save_cwd = os.getcwd()
		print "~ Installing parent pom..."
		os.chdir(os.path.join(module_dir, 'resources/play-parent'))
		os.system('mvn clean install')
		os.chdir(save_cwd)

	if play_command == 'new' or play_command == "mvn:init":
		module_dir = inspect.getfile(inspect.currentframe()).replace("commands.py","")
		print module_dir
		os.system('play mvn:install')
		if os.path.exists('pom.xml'):
			print "Existing pom.xml will be backed up to pom.xml.bak"
			shutil.copyfile('pom.xml', 'pom.xml.bak')
		shutil.copyfile(os.path.join(module_dir,'resources/pom.xml'), os.path.join(application_path, 'pom.xml'))

	if play_command == 'mvn:update' or play_command == 'mvn:up':
		print "~"
		print "~ Retriving dependencies..."
		print "~"
		os.system('mvn dependency:copy-dependencies')
		os.system('play mvn:src')

	if play_command == 'mvn:refresh' or play_command == 'mvn:re':
		print "~"
		print "~ Refresh dependencies..."
		print "~"
		os.system('mvn clean')
		os.system('play mvn:up')

	if play_command == 'mvn:sources' or play_command == 'mvn:src':
		print "~"
		print "~ Retriving dependencies sources..."
		print "~"
		os.system('mvn dependency:copy-dependencies -Dclassifier=sources')

	if play_command == 'mvn:play-dependency-sources' or play_command == 'mvn:play-src':
		print "~"
		print "~ Retriving Play's dependencies sources..."
		print "~"
		os.system('mvn dependency:copy-dependencies -Pplay-src')

	sys.exit(0)
