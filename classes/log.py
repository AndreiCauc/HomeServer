HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def disable():
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''

def info(title, message):
	print("{}[INFO][{}] {}{}".format(OKBLUE, title, message, ENDC))

def success(title, message):
	print("{}[INFO][{}] {}{}".format(OKGREEN, title, message, ENDC))


def warn(title, message):
	print("{}[WARNING][{}] {}{}".format(WARNING, title, message, ENDC))

def error(title, message):
        print("{}[ERROR][{}] {}{}".format(FAIL, title, message, ENDC))


def testColors():
	print "0\t\033[0m coloured! \033[m\n";
	print "1\t\033[1m coloured! \033[m\n";
	print "4\t\033[4m coloured! \033[m\n";
	print "7\t\033[7m coloured! \033[m\n";
	print "31\t\033[31m coloured! \033[m\n";
	print "32\t\033[32m coloured! \033[m\n";
	print "33\t\033[33m coloured! \033[m\n";
	print "34\t\033[34m coloured! \033[m\n";
	print "35\t\033[35m coloured! \033[m\n";
	print "36\t\033[36m coloured! \033[m\n";
	print "37\t\033[37m coloured! \033[m\n";
	print "38\t\033[38m coloured! \033[m\n";
	print "39\t\033[39m coloured! \033[m\n";
	print "40\t\033[40m coloured! \033[m\n";
	print "41\t\033[41m coloured! \033[m\n";
	print "42\t\033[42m coloured! \033[m\n";
	print "43\t\033[43m coloured! \033[m\n";
	print "44\t\033[44m coloured! \033[m\n";
	print "45\t\033[45m coloured! \033[m\n";
	print "46\t\033[46m coloured! \033[m\n";
	print "47\t\033[47m coloured! \033[m\n";
	print "90\t\033[90m coloured! \033[m\n";
	print "91\t\033[91m coloured! \033[m\n";
	print "92\t\033[92m coloured! \033[m\n";
	print "93\t\033[93m coloured! \033[m\n";
	print "94\t\033[94m coloured! \033[m\n";
	print "95\t\033[95m coloured! \033[m\n";
	print "96\t\033[96m coloured! \033[m\n";
	print "97\t\033[97m coloured! \033[m\n";
	print "98\t\033[98m coloured! \033[m\n";
	print "99\t\033[99m coloured! \033[m\n";
	print "100\t\033[100m coloured! \033[m\n";
	print "101\t\033[101m coloured! \033[m\n";
	print "102\t\033[102m coloured! \033[m\n";
	print "103\t\033[103m coloured! \033[m\n";
	print "104\t\033[104m coloured! \033[m\n";
	print "105\t\033[105m coloured! \033[m\n";
	print "106\t\033[106m coloured! \033[m\n";
	print "107\t\033[107m coloured! \033[m\n";
	print "108\t\033[108m coloured! \033[m\n";
