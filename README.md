

# GitHub API Integration (Django + DRF)

A simple **Django REST Framework (DRF)** project to integrate with the **GitHub Public API**.  
It allows you to fetch a GitHub user's profile and repositories, store them in a database (SQLite/MySQL), and query them later via APIs.

---

## 🚀 Features
- Fetch GitHub user profile details:
  - Name  
  - Public repositories count  
  - Followers & Following  
  - Account creation date  
- Fetch and store **all repositories** of a user:
  - Repository name  
  - Primary language  
  - Star count  
  - Fork count  
  - Last updated date  
- Store **users** and **repositories** in database with foreign key relationship.
- Retrieve stored user/repository data from database.
- Error handling for invalid usernames (404).

---

## ⚙️ Tech Stack
- Python 3.x
- Django 5.x
- Django REST Framework (DRF)
- SQLite (default) or MySQL

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/juniap321/Github-api.git
   cd Github-api
````

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

---

## 🔗 API Endpoints

### 1. Fetch & Save User + Repositories

**POST** `/api/github/fetch-user/`

**Request Body:**

```json
{
  "username": "octocat"
}
```

**Response Example:**

```json
{
  "id": 1,
  "username": "octocat",
  "name": "The Octocat",
  "public_repos_count": 8,
  "followers_count": 100,
  "following_count": 0,
  "account_creation_date": "2011-01-25T18:44:36Z",
  "repositories": [
    {
      "id": 1,
      "name": "Hello-World",
      "primary_language": "Ruby",
      "star_count": 1600,
      "fork_count": 1200,
      "last_updated_date": "2025-01-10T12:00:00Z"
    }
  ]
}
```

---

### 2. Get User Details (from DB)

**GET** `/api/github/user/<username>/`

**Example:**
`/api/github/user/octocat/`

---

### 3. Get Repositories (from DB)

**GET** `/api/github/user/<username>/repos/`

**Example:**
`/api/github/user/octocat/repos/`

---

## 🛑 Error Handling

* Invalid username (404):

```json
{"error": "Invalid GitHub username"}
```

* Missing username in request:

```json
{"error": "Username is required"}
```

---

## 🧪 Sample Valid GitHub Users

* `octocat`
* `torvalds`
* `JakeWharton`
* `mojombo`
* `pjhyett`

## ❌ Sample Invalid GitHub Users

* `thisuserdoesnotexist12345`
* `invalid_account_xyz`
* `notarealuser_999`
* `fake_github_user_test`
* `ghost123fake`

