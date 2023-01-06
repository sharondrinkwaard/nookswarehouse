# Nooks Warehouse

Welcome to Nooks Warehouse, a shop for all your household products and furniture. This shop is based in the Netherlands and eventually will expand to more countries in the EU. 

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
For now I am displaying example products and I used the same data for this as in the Boutique Ado walkthrough. So these are not real products. 

To display these products, I used the models, views and database from the walkthrough project, because this is the quickest and easiest way to display the products for now. 

<strong>NOTE:</strong> To show that I understand how rendering these products and categories work, I made some changes and I added extra data to these files myself. You can find them under the category 'baby'.

After submitting, I am going to delete all the products and implement the plug-in from VidaXL to start my dropshipping business. 


## Left to Implement
- As soon as I submit this project, I am going to start replacing the current products with real products. So that visitors can actually buy physical products. I am going to use a dropshipping plug-in from VidaXl WooCommerce for the inventory.  
-	I am also going to add a Pinterest link to the Pinterest account for the affiliate marketing part of this business.


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



## Agile
---
When planning this project, I started writing the epics first. Then I broke them down into user stories. For this I have created an Excel sheet and a kanban board. I prefered the Excel sheet because for me it created and clearer overview than the kanban board.

For this portfolio project the estimated time is 3 weeks.
For the total project (including the features left to implement) I am estimating 6 weeks

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

- <strong>Link from products to product detail page</strong> When clicking on a product image, nothing would happen. I figured out that I swapped the urls to link would direct to the page I was currently on. I solved this by swapping the links.

### Unsolved
---
There are no bugs left unsolved.


## Credits
---
- [Stackoverflow]()
- [Google Translate]()
- [W3Schools]()
- [Django Documentation]()
- [Bootstrap Documentation]()

### Acknowledgments
- Thank you Code Institute and mentor Daisy for guiding me through this project. 
- Thank you fellow students on Slack for the contact and motivation.




BEFORE DEPLOYMENT:
-	Html tab spaces allemaal gelijk zetten
- dissable collect static?

