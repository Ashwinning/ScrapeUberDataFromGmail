


#Accepts a soup and returns the total fare
def GetDetails(soup):
    details = {}
    details['totalPrice'] = soup.find_all("td", class_="totalPrice")[0].string
    dateAndRideType = soup.find_all("td", class_="rideInfo gray")[0].string
    keyVal = dateAndRideType.split('|')
    details['date'] = keyVal[0].strip()
    details['rideType'] = keyVal[1].strip()
    startTime = soup.find_all("td", class_="firstAddress")[0].contents[0].string
    details['startTime']=startTime.split("|")[0].strip()
    endTime = soup.find_all("td", class_="address")[1].contents[0].string
    details['endTime']=endTime.split("|")[0].strip()
    details['startAddress'] = soup.find_all("td", class_="firstAddress")[0].contents[1].string.strip()
    details['endAddress'] = soup.find_all("td", class_="address")[0].contents[1].string.strip()
    details['distance'] = soup.find_all("td", class_="tripInfo")[0].string.strip()
    details['time'] = soup.find_all("td", class_="tripInfo")[1].string.strip()
    return details
