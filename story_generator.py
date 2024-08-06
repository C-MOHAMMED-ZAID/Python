import random
when=['A few years ago','yesterday','last night','A long time ago','On 20th Jan']
who=['a rabbit','an elephant','a mouse','a turtle','a cat']
name=['Ali','miriam','daniel','harry','starwalker']
residence=['Barcelona','india','germany','venice','england']
went=['cinema','university','seminar','school','laundry']
happened=['made a lot of friends','eats a burger','found a secret key','solved a mistery','wrote a book']
print(random.choice(when)+ ' , '+ random.choice(who) + ' that lived in '+ random.choice(residence)+', went to the '+random.choice(went)+' and '+random.choice(happened))
