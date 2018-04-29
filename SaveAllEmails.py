import gmail
from Settings import *


#Initialize this at the beginning of the lifecycle.
getSettings = GetSettings()

g = gmail.login(settings['username'], settings['password'])

emails =g.mailbox('advantEdge Commute').mail()
print str(len(emails)) + " emails found"
i = 0;
for email in emails:
    email.fetch()
    file = open("emails/"+ str(i) +".html","w")
    file.write(email.html)
    file.close()
    i+=1
