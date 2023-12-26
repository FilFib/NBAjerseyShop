# NBAjerseyShop 

Welcome to the NBA Jersey Shop, online store selling NBA player jerseys.



## Installation process:

1. Clone the repository to your local computer:

    ```
    $ git clone 'https://github.com/FilFib/NBAjesrseyShop.git'
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
