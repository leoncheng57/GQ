import google, urllib2, requests, bs4, re
import regex

def get_text(search, n):                                                        
    url_list=[]                                                                 
    search_results = google.search(search, num=n,start=0,stop=n).next()         
    for url in search_results:                                                  
        url_list.append(url)                                                    
    text = []
    for url in url_list:
        try:
            r = urllib2.Request(url)
            u = urllib2.urlopen(r)
            page = u.read()
            soup = bs4.BeautifulSoup(page,'html')
            raw = soup.get_text()
            
            reg = re.sub("[\t\n ]"," ",raw)
            text.append(reg)
        except:
            pass
    return text
    
#To test each functions
if __name__=='__main__':      
    input = raw_input("Enter stuff: ")                                    
    text = get_text(input)
    for i in text:
        print i

    #input = raw_input("Enter some names: ")                                    
    #result_name = re.findall(regex.name, input)
    
    #input = raw_input("Enter some dates: ")
    #result_date = re.findall(regex.date, input)
    

    #print("Name results: ")
    #print result_name

    #print("Date results: ")
    #print result_date
