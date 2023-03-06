# Nooks Warehouse

Welcome to Nooks Warehouse, a shop for all your household products, furniture and clothes. This shop is based in the Netherlands and eventually will expand to more countries in the EU. 
Note that for now this is a fictional website. All payments made through this website won't actually deliver a product, but are seen as 'tests'.

MOCKUP PICTURE

## Features
---
### Favicon
### Navigation Bar
### Promoted Categories
### Promoted Products
### About Us
### Gallery
### Contact
### Footer

### Products
---
For now I am displaying example products and I used the same data fixtures for this as in the Boutique Ado walkthrough. So these are not real products. These products will be updated in the future.

<strong>NOTE:</strong> To show that I understand how rendering these products and categories work, I made some changes and I added extra data to these files myself. You can find them under the category 'baby & kids'.

After submitting, I am going to delete all the products and implement the wooCommerce plug-in to start my dropshipping business. 


## Left to Implement
- <strong>Products.</strong>As soon as I submit this project, I am going to start replacing the current products with real products. So that visitors can actually buy physical products. I am going to use a dropshipping WooCommerce plug-in for the inventory.  
-	<strong>Pinterest.</strong>I am also going to add a Pinterest link to the Pinterest account for the affiliate marketing part of this business.
- <strong>Design.</strong> I'm not content about the design of this project. Due to a time limit I decided to not put too much time in it and focus on the technical side first.
- <strong>Email conformations.</strong>I would like to send an automated email to the client who made a purchase.
- <strong>Messages and signals.</strong> For now I commented out the messages I would like to display. Whenever someone makes a purchase, edited the shoppingcart, or added a product. I ran out of time to get this to work and decided to leave it as a feature left to implement.
- <strong>Identation.</strong> I played around with different identation tabs. 4 and 2. This is why some pages of html are in 4 tabs and others in 2. I am going to set these to the same value of tabs which will be 2. 
- <strong>Grammar and spelling.</strong> As English is my second language, there might be some grammar or spelling mistakes. I want to correct these in the future. 
- <strong>Filtering and sorting.</strong> I want the user to be able to sort and filter the products. 
- <strong>Unsolved bugs.</strong> I want to fix all unsolved bugs. 


## Design
---
- I used Balsamiq to create a first picture of what this project would look like.
- On [Coolors](https://coolors.co/) I created a colour pallete so I know what colours match and look nice together. The colours I used are:
	- #25283D
	- #C4A29E
	- #FFFF82
	- #087F8C
	- #97C8EB

I might not have used all of them at this moment, but I will in the future.

## Libraries & Installations
---
- Django Allauth
- Summernote 
- Pillow
- Crispy forms
- Stripe Payments



## Agile
---
When planning this project, I started writing the epics first. Then I broke them down into user stories. For this I have created an Excel sheet and a kanban board. I prefered the Excel sheet because for me it created and clearer overview than the kanban board.

For this portfolio project the estimated time is 6 weeks.
For the total project (including the features left to implement) I am estimating 12 weeks

- LINK TO KANBAN BOARD
- SCREENSHOT OF EXCEL SHEET

## SEO
---
- I added Meta tags to add keywords and a description
- I used Semantic Code like a header, h1 and h2 on every page, several sections, footer etc.
- I googled what would be correct keywords to use
- Alt attributes on images where possible
- I used Facebook and Instagram marketing and will use Pinterest marketing in the future as well.
- I am using Email marketing

## Testing
---
## Bugs
---
### Solved
---
- <strong>Anchor tags to another page</strong> I didn't know how to add anchor tags to another page. So by only placing an anchor tag, the result was that the link was not doing anything unless the link was on the same page I was currently on. This was an issue and I solved it with help from [Stackoverflow](https://stackoverflow.com/questions/31643670/link-a-div-in-another-page-in-url-with-an-anchor-tag-django). How I solved it:
```
	href="{% url 'customer_service' %}#terms-conditions"
```

- <strong>Link from products to product detail page</strong> When clicking on a product image, nothing would happen. I figured out that I swapped the urls. The link would direct to the page I was currently on. I solved this by swapping the links.

- <strong>I added a Booleandfield to the products model instead of a Charfield.</strong> I made migrations for this using <italic>python3 manage.py makemigrations</italic>. They couldn't be applied using <italic>python3 manage.py migrate</italic> because the requirements of a booleanfield didn't match the ones I was trying to apply. This resulted in an error. By using <italic>showmigrations</italic> I figured out that for every change I tried to make, the first one was still the one with an typo in it and was preventing all other migrations to be applied. 

	I solved this by deleting all unapplied (but made migrations) from the products app inside the migrations folder. Without having to clear the whole database. I made sure to create a new migration for the changes and this time it worked and the website was running again. 

- <strong></strong>

### Unsolved
---
- <strong>Product size.</strong> After making a purchase, the customer is directed to the success page. On this page is all the billing, shipping and product information displayed. Except the size of the purchased product. Sometimes it is being shown, and other times it is not. This also happens whenever the product is being updated in the shoppingcart itself. When just added to the shoppingcart, the size is dislayed. But (sometimes) when the product quantity is updated, it disappears. 

## Deployment
---

## Credits
---
- [Stackoverflow]()
- [Google Translate]()
- [W3Schools]()
- [Django Documentation]()
- [Bootstrap Documentation]()
- [Stripe Documentation]()

### Acknowledgments
- Thank you Code Institute and mentor Daisy for guiding me through this project. 
- Thank you fellow students on Slack for the contact and motivation.
- Thank you Tutor support for guiding me in the right direction.




BEFORE DEPLOYMENT:
-	Html tab spaces allemaal gelijk zetten
- dissable collect static?

