import getopt
import sys
from src.run import run

argumentList = sys.argv[1:]
options = "ha:t:p:"

try:
    arguments, values = getopt.getopt(argumentList, options)
    archive = False
    threads = False
    parameters = False
     
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h"):
            print("""Usage: python main.py -h <= Help
               -a <Str:Archive> <= Input Database File (JSON extension)
               -t <Int:Threads> <= Number of Threads
               -p <Int:Parameters> <= Execution Parameters""")
             
        elif currentArgument in ("-a"):
            archive = currentValue
             
        elif currentArgument in ("-t"):
            threads = currentValue
        
        elif currentArgument in ("-p"):
            parameters = currentValue
    
    if archive:
        if threads:
            if parameters:
                run(archive, threads, parameters)
            else:
                print("Need parameters")  
        else:
            print("Need threads")    
    else:
        print("Need archive")
             
except getopt.error as err:
    print(str(err))