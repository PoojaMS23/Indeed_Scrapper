# Indeed_Scraper

The main objective of this project was to build a functional web scraper using Python. Here, I explored the Data Analyst jobs posted on the Indeed Job portal using Python and its libraries such as Beautiful_Soup, Requests, Pandas etc.   

BeautifulSoup is imported from the bs4 for pulling data out of HTML and XML files. It also allows users to parse certain parts of 	them without any hassle. It only fetches the contents of the URL that you give and then stops. The `Crawler` has the code to scrap the Indeed job portal. The code runs to hit the given URL and collects the information such as Location and Synopsis from the Job posts. 

The tkinter package is a standard Python framework used to create the graphical user interface. The `Main_indeed` runs the code to display the interface. The below image represents the user interface where the widgets are displayed in an understandable user format.

![image](https://user-images.githubusercontent.com/56773865/179622136-6d14507f-e1e5-4d8d-956f-a3971f1d13f6.png)

The web scraping is done once the crawler widget/button is pressed. This can take some time to collect the data from indeed and the collected information is then stored in CSV file [here it is `Indeed_Project`]. 

In the near future, I’ll implement code to collect more information such as title, Company name etc to examine and perform exploratory data analysis.

#### Thank you!
