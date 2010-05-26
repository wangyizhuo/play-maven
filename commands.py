import sys,os,inspect

if play_command == 'new' or play_command == "mvn:init":
    module_dir = inspect.getfile(inspect.currentframe()).replace("commands.py","")
    save_cwd = os.getcwd()
    print "~ Installing parent pom..."
    os.chdir(os.path.join(module_dir, 'resources/play-parent'))
    os.system('mvn clean install')
    os.chdir(save_cwd)
    shutil.copyfile(os.path.join(module_dir,'resources/pom.xml'), os.path.join(application_path, 'pom.xml'))

if play_command == 'mvn:up' or play_command == 'mvn:update':
    print "~"
    print "~ Retriving dependencies..."
    print "~"
    os.system('mvn dependency:copy-dependencies')

if play_command == 'mvn:re' or play_command == 'mvn:refresh':
    print "~"
    print "~ Refresh dependencies..."
    print "~"
    os.system('mvn clean dependency:copy-dependencies')

if play_command == 'mvn:src' or play_command == 'mvn:source':
    print "~"
    print "~ Retriving dependencies sources..."
    print "~"
    os.system('mvn dependency:copy-dependencies -Dclassifier=sources')

sys.exit(0)    
