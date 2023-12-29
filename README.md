# NBAjerseyShop 

Welcome to the NBA Jersey Shop, online store selling NBA player jerseys.

![Homepage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/homepage.PNG?raw=true)

## Table of contents
* [Installation process](#installation-process)
* [Technologies](#technologies)
* [Features](#features)
* [About authors](#authors)

## Installation process:

1. Clone the repository to your local computer:

    ```
    $ git clone 'https://github.com/FilFib/NBAjerseyShop.git'
    ```

2. Navigate to the project directory:

    ```
    $ cd NBAjesrseyShop
    ```

3. (Optional) It is recommended to create and activate a Python virtual environment:

    ```
    $ python -m venv venv
    ```
    Activate for windows:
    ```
    $ python venv\Scripts\activate
    ```
    Activate for Linux:
    ```
    $ python venv/bin/activate
    ```

4. Install the required dependencies:

    ```
    $ pip install -r requirements.txt
    ```

5. Create database 'db.sqlite3' using migration:

    ```
    $ python manage.py migrate
    ```

6. Run the Django development server:

    ```
    $ python manage.py runserver
    ```

    The application will be available at http://localhost:8000/.

7. (Optional) Change the database to the one available at the link below with all NBA teams saved and 10 sample player jerseys:

    https://drive.google.com/drive/folders/1vmaOkXcj8qwCzvUDUeTdR3fSuZd0w0zx?usp=sharing 



## Technologies

### HTML5, CSS3 and Bootstrap

For the frontend, we used HTML5, CSS3 and Bootstrap5, which allowed us to create an intuitive and user-friendly user interface.

### Python and Django

We provided a strong backend foundation by using Python 3.11 and Django 4.2. Python offers the latest features, bug fixes and optimizations, which contributes to effective and modern application development. Django 4.2, as a high-level web framework, provides tools for quickly creating solid web applications.



## Features

The aim of the project was to create an online store enabling users to buy NBA players' jerseys, where orders and adding products are handled by the administrator. The website was created to improve skills in the Django framework, as a culmination of the comprehensive "Python from scratch" course at Software Development Acadamy.

### Accounts app:
An application created to manage user accounts. Enables registration, login and logout.

Registrtaion:

![Registrationpage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/registrationpage.PNG?raw=true)

Login:

![Loginpage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/loginpage.PNG?raw=true)

### Shop app:
The shop application is responsible for displaying products on the home page and on the page with jerseys of a specific selected team, as well as on the page with details of the selected product.

Homepage:

![Homepage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/homepage.PNG?raw=true)

Team jerseys page:

![Teampage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/teampage.PNG?raw=true)

Jersey detail page:

![Jerseydetail](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/jerseydetail.PNG?raw=true)

### Cart app:

It allows you to view the contents of the basket, add and remove products, as well as update the quantity of the selected product. Everything was implemented using sessions.

Cart view:

![Cart](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/cart.PNG?raw=true)

### Orders app:

Responsible for placing orders and saving them to the database. This application also allows you to view previously placed orders.

Order page:

![Orderpage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/orderpage.PNG?raw=true)

Thank you page after placing your order:

![Orderpage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/ordercreatedpage.PNG?raw=true)

User's order page:

![Orderpage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/orderspage.PNG?raw=true)

### Administration panel:

All order processing and adding products is possible thanks to the administration panel.
![Orderpage](https://github.com/FilFib/NBAjerseyShop/blob/develop/README_img/adminpanel.PNG?raw=true)

## Authors:

<table>
  <tr>
      <ul>
        <b>Filip Fibakiewicz</b>
        <p>Junior Python Developer</p>
        <li><a href="https://www.linkedin.com/in/filfib/">LinkedIn Profile</a></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <ul>
        <b>Rafał Ćwikła</b>
        <p>Junior Python Developer</p>
        <li><a href="https://www.linkedin.com/in/rafalcwikla/">LinkedIn Profile</a></li>
      </ul>
    </td>
  </tr>
</table>
