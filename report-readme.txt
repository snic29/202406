To run this report.py program, 

        python report.py -file path/to/your/jsonfile.json -config path/to/your/configfile.txt  

python program to parse an input json file provided as argument at program execution using -file option. 
The program will use a configuration file , provided as parameter using -config option , to instruct the program on the actual field to be extracted. For example: if json file has following format:
{
  "a" : {
     "l11": {
       "l12" : {
           "Report" : "v1",
	   "Result" : {
		"f11": "POS",
		"f12": "NEG",
		......
		"f1n": "NEG"
	    }
         } 
      },
     .......
     "lm1": {
       "lm2" : {
           "Report" : "vm",
	   "Result" : {
		"fm1": "NEG",
		"fm2": "POS",
		......
		"fmn": "POS"
	    }
         } 
      }
}
and config file has format is :
a.*.*.Report
a.*.*.Result{"POS"}
a.*.*.Result{"NEG"}
where * is the level of chaining in json file to be skipped disregarding the name of the field.
a is the first level, a.* is the second, a.*.* is the third level 
a.*.*.Report is the value of the fourth level of associated to name "Report" for that entry
a.*.*.Result{"POS"} is the list of comma delimited names of the forth level which have the same value ="POS"
a.*.*.Result{"NEG"} is the list of comma delimited names of the forth level which have the same value ="NEG"

will produce the output like:
Report : v1
POS : f11..
NEG : f12,.. ,f1n
-----------
....
-----------
Report : vm
POS : fm2,..,fmn
NEG : fm1,..

