# Goodreads

## Contributors
(Emma Westerhoff)[https://github.com/ewesterhoff]

(Uma Desai)[https://github.com/umadesai]

(Emma Price)[https://github.com/ejprice54321]

## General Project Description
This is a project that is aimed at crawling and scraping through the goodreads website and storing all of the data in a MySQL database. This data includes information about authors and books including reviews of the book. Eventually this data will be used to develop a data analysis and visualization of something on goodreads. 
Possible ideas include:
- sentiment analysis of reviews, compare to ratings
- analyzing for patterns between date of publishing of books and popularity
- visualizing popularity of books over time

## Libraries Used:
- urllib
- beautifulSoup
- pymysql
- time
- *Line 7 in database.py should be changes to fit individual user and password information

## Object Outline (also the data collected)

Books
- Title
- Description
- Author
- Date Published
- Book Type
- Pages
- Rating Average
- Characters
- Awards

Author
- Name
- Website
- Birth
- Death
- Biography

Reviews
- Reviewer Name
- Likes
- Date
- Content
- Rating
