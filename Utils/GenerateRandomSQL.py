from SQLOperations import *
import sys

for _ in range (int(sys.argv[1])):
	time = "-".join(str(datetime.datetime.now()).split(" "))
	sql_path = "some path"+ time + ".sql"
	tb_cr, proc = RandomProcedure("db")

	with open(sql_path,"w+") as file:
    		file.write(use_db("db")+'\n')
    		file.write(tb_cr+'\n')
    		file.write('\n'.join(proc) + '\n')
    		file.close()

print ("SQL files generated!")
