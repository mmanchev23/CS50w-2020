# CS50w-2020

## All 6 exam projects from CS50w-2020

### Technologies:
<ul>
    <li>
        Programming Languages - Python, Javascript, HTML5, CSS3
        <br/>
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
        <img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
        <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
        <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/>
    </li>
    <li>
        Frameworks - Django
        <br/>
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
    </li>
    <li>
        Database - SQLite 3
        <br/>
        <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
    </li>
    <li>
        Version Controll Systems - Git and Github
        <br/>
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
        <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </li>
    <li>
        IDE - Visual Studio Code
        <br/>
        <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </li>
</ul>

### Projects:
1. Project 0 - [Search](https://github.com/mmanchev23/CS50w-2020/tree/main/Project%200%20-%20Search)
2. Project 1 - [Wiki](https://github.com/mmanchev23/CS50w-2020/tree/main/Project%201%20-%20Wiki)
3. project 2 - [Commerce](https://github.com/mmanchev23/CS50w-2020/tree/main/Project%202%20-%20Commerce)
4. Project 3 - [Mail](https://github.com/mmanchev23/CS50w-2020/tree/main/Project%203%20-%20Mail)
5. Project 4 - [Network](https://github.com/mmanchev23/CS50w-2020/tree/main/Project%204%20%20-%20Network)
6. Project 5 - [Capstone](https://github.com/mmanchev23/CS50w-2020/tree/main/Project%205%20-%20Capstone)

### How to start the projects?
<ol>
    <li>
        Open the selected project in the console, IDE or text editor.
    </li>
    <li>
        Install virtual environment (if you haven't already!!!)
        <br/>
        <code>
            pip install pipenv
        </code>
    </li>
    <li>
        Open the virtual environment:
        <br/>
        <code>
            pipenv shell
        </code>
    </li>
    <li>
        Install the required packages:
        <br/>
        <code>
            pipenv install -r requirements.py
        </code>
    </li>
    <li>
        Navigate to the directory with the "manage.py" file
        <br/>
        <code>
            cd "path\to\folder\with\manage.py"
        </code>
    </li>
    <li>
        Run the following commands:
        <br/>
        <code>
            1. python manage.py makemigrations
        </code>
        <br/>
        <code>
            2. python manage.py migrate
        </code>
        <br/>
        <code>
            3. python manage.py runserver
        </code>
    </li>
    <li>
        Open the following link:
        <br/>
        <code>
            http://127.0.0.1:8000/
        </code>
    </li>
</ol>

### Files & Directories
- `models.py` - ORM auth model. Contains an Code class which has user and hashed reset password code.
- `urls.py` - Contains all url paths for authentication, like login, sign up, as well as logout.
- `views.py` - Contains all view functions for authentication, like login, as well as logout.
- `templates` - Holds all html files.
- `static` - Holds all static files.
    - `css` - Contain all css files for styling the website.
    - `js` - Contains all JavaScript files for manipulating the DOM functionalities.
