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
	def option_query(cat): 
		print "What are the options? Type done when you're finished"
		i = 1
		options = []
		cat = (cat, options)
		option = raw_input("Option " + str(i) + ': '); 
		while option != "done":
			newCat = (cat, options + [option])
			i+=1
			return newCat
			

	if option != "no":
		while option!="done":
			cat2 = option_query(cat)
	end = len(cat2) - 1
	print "ok, " + cat2[0] + " can be: "
	for c in cat2[1]:
		print cat2[c]

cat_query()

