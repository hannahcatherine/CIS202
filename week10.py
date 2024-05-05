monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November' , 'December']

datestring = input('Enter a date in the formal mm/dd/yyyy: ')

datelist = datestring.split('/')

month = int(datelist[0])
day = datelist [1]
year = datelist [2]

month = monthlist[month-1]

dateprint = month + ' ' + day + ', ' + year

print (dateprint) 
