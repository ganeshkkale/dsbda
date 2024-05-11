import requests
import bs4

requests1 = requests.get("https://www.amazon.in/Apple-MacBook-Chip-13-inch256GB/dp/B08N5W4NNB/ref=sr_1_1?crid=1J2JI0HJBX9JV&keywords=macbook+air+m1&qid=1680253105&sprefix=macbook+air+m%2Caps%2C229&sr=8-1")
print("REQUEST 1 = \n", requests1 , "\n")
print("CONTENTS OF REQUEST 1 = \n", requests1.content , "\n")
soup = bs4.BeautifulSoup(requests1.text)
print(soup)

reviews = soup.find_all( 'div' , { 'class' : 'a-expander-content reviewText review-text-content a-expanderpartial-collapse-content'}); # or findAll
print(reviews)
count = 1
for review in reviews :
 print("\nFETCHING REVIEW" , str(count), "\n")
 print(review.get_text() , "\n\n")
 count = count + 1
ratings = soup.find ( 'div' , {'class' : 'a-row a-spacing-medium averageStarRatingNumerical' }).get_text()
print(ratings)
individual_ratings = soup.find_all( 'i' , { 'class' : 'a-icon a-icon-star a-star-4 review-rating' })
for ind_r in individual_ratings:
 print ( ind_r.get_text())
customer_name_list = soup.find_all( 'div' , { 'class' : 'a-profile-content' });