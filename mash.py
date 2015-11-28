#!/usr/bin/python



print"********.-.*********,---.    ,---.   ____       .-'''-. .---.  .---."  
print"*******/   \********|    \  /    | .'  __ `.   / _     \|   |  |_ _|"  
print"******|     |*******|  ,  \/  ,  |/   '  \  \ (`' )/`--'|   |  ( ' )" 
print"**099 \_( )_/9990***|  |\_   /|  ||___|  /  |(_ o _).   |   '-(_{;}_)"
print"***099(_ o _)990****|  _( )_/ |  |   _.-`   | (_,_). '. |      (_,_)"
print"****009(_,_)900*****| (_ o _) |  |.'   _    |.---.  \  :| _ _--.   |"
print"******0099900*******|  (_,_)  |  ||  _( )_  |\    `-'  ||( ' ) |   |"
print"********000*********|  |      |  |\ (_ o _) / \       / (_{;}_)|   |"
print"********************'--'      '--' '.(_,_).'   `-...-'  '(_,_) '---'"
print""                                                  
print"Lets Play!"



def cat_query():
	cat = raw_input("Type a Category: ");
	print "Cool! ", cat, " is a great category."
	option = raw_input("Do you want to keep it? (yes/no)");
	def option_query(cat, i): 
		print "What are the options? Type done when you're finished"
		options = []
		cat = (cat, options)
		option = raw_input("Option " + str(i) + ': '); 
		if option.lower() not in ("done"):
			newCat = (cat, options + [option])
			i+=1
			return newCat
			option_query(newCat, i)
			

	if option not in ("no", "done"):
		i = 1
		while option.lower() !="done":
			cat2 = option_query(cat, i)
			i += 1
		end = len(cat2) - 1
		print "ok, " + cat2[0] + " can be: "
		for c in cat2[1]:
			print cat2[c]

cat_query()

