# Contributing to Hacktoberfest @ GDG Babcock 2025

First off, thank you for your interest in contributing! 🎉
This project is part o---

## 📌 How to Contribute

1. **Fork the repository**est 2025**, organized by **GDG Babcock**, to encourage open source contributions and help beginners get started with Git and GitHub. Contributions aren't limited to code. You can improve documentation, design, or even translations. Learn more from this great guide: [Open Source Non-Code Contributions](https://github.com/readme/featured/open-source-non-code-contributions).

We're excited to have you on board 🚀.

---

## 📋 Table of Contents

- [Project Setup](#-project-setup)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Docker Setup](#docker-setup)
- [How to Contribute](#-how-to-contribute)
- [Branch and PR Flow](#-branch-and-pr-flow)
- [Commit Message Style](#-commit-message-style)
- [Contribution Guidelines](#-contribution-guidelines)
- [What You Can Contribute](#-what-you-can-contribute)
- [Code of Conduct](#-code-of-conduct)

---

## 🛠️ Project Setup

This project consists of two main components:
- **Backend**: FastAPI (Python) REST API
- **Frontend**: React (Vite) application

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Git** - [Download & Install Git](https://git-scm.com/downloads)
- **Node.js** (v16 or higher) and **npm** - [Download & Install Node.js](https://nodejs.org/)
- **Python** (v3.8 or higher) - [Download & Install Python](https://www.python.org/downloads/)
- **Docker** (optional, for containerized setup) - [Download & Install Docker](https://www.docker.com/products/docker-desktop)

### Backend Setup

Follow these steps to set up the FastAPI backend locally:

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```bash
   # From the backend directory
   uvicorn app.main:app --reload
   ```
   
   The API will be available at `http://localhost:8000`
   
5. **Access API documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

**Backend Dependencies:**
- FastAPI - Web framework
- Uvicorn - ASGI server
- Pydantic - Data validation
- ReportLab - PDF generation
- Pillow - Image processing
- SQLAlchemy - Database ORM

### Frontend Setup

Follow these steps to set up the React frontend locally:

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```
   
   The application will be available at `http://localhost:5173` (or another port if 5173 is in use)

4. **Build for production** (optional):
   ```bash
   npm run build
   ```

**Frontend Dependencies:**
- React - UI library
- Vite - Build tool and dev server
- ESLint - Code linting

### Docker Setup

If you prefer to use Docker for easier setup:

1. **Ensure Docker and Docker Compose are installed** on your system.

2. **From the root directory**, run:
   ```bash
   docker-compose up --build
   ```

3. **Access the services:**
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000`

4. **Stop the services:**
   ```bash
   docker-compose down
   ```

---

## 📌 How to Contributing to Hacktoberfest @ GDG Babcock 2025

First off, thank you for your interest in contributing! 🎉
This project is part of **Hacktoberfest 2025**, organized by **GDG Babcock**, to encourage open source contributions and help beginners get started with Git and GitHub. Contributions aren’t limited to code. You can improve documentation, design, or even translations. Learn more from this great guide: [Open Source Non-Code Contributions](https://github.com/readme/featured/open-source-non-code-contributions).

We’re excited to have you on board 🚀.

---

## 📌 How to Contribute

1. **Fork the repository**

   * Click the **Fork** button (top-right corner of this repo).

2. **Clone your fork**

   ```bash
   git clone https://github.com/GDGBabcockUniversity/gdg-babcock-hacktoberfest-2025
   cd gdg-babcock-hacktoberfest-2025
   ```

3. **Create a new branch**

   * Branch names should be descriptive.

   ```bash
   git checkout -b fix/typo-in-readme
   # or
   git checkout -b feature/add-javascript-example
   ```

4. **Make your changes**

   * Follow the project’s coding style.
   * Ensure your changes are meaningful and documented.

5. **Commit your changes**

   ```bash
   git add .
   git commit -m "Add: new JavaScript Hello World example"
   ```

6. **Push your branch**

   ```bash
   git push origin feature/add-javascript-example
   ```

7. **Open a Pull Request (PR)**

   * Go to the original repo and click **New Pull Request**.
   * Clearly describe your contribution.

---

## 🌿 Branch and PR Flow

### Branch Naming Convention

Use descriptive branch names that clearly indicate the purpose of your changes:

- **Feature branches**: `feature/description-of-feature`
  - Example: `feature/add-certificate-templates`
  
- **Bug fixes**: `fix/description-of-bug`
  - Example: `fix/certificate-generation-error`
  
- **Documentation**: `docs/description-of-change`
  - Example: `docs/update-setup-instructions`
  
- **Refactoring**: `refactor/description-of-refactor`
  - Example: `refactor/improve-api-structure`
  
- **Chores** (dependency updates, config changes): `chore/description`
  - Example: `chore/update-dependencies`

### Pull Request Process

1. **Before creating a PR:**
   - Ensure your code works locally without errors
   - Test both backend and frontend if you made changes to both
   - Update documentation if you added new features
   - Make sure your branch is up to date with the main branch

2. **Creating a PR:**
   - Use a clear and descriptive title
   - Provide a detailed description of what your PR does
   - Reference any related issues (e.g., "Closes #123")
   - Add screenshots/videos if your changes affect the UI
   - Request review from maintainers

3. **PR Review Process:**
   - Maintainers will review your PR
   - Address any feedback or requested changes
   - Once approved, your PR will be merged
   - Delete your feature branch after merging

4. **Keep your fork updated:**
   ```bash
   # Add upstream remote (only needed once)
   git remote add upstream https://github.com/Kshitiz-2027/gdg-babcock-hacktoberfest-2025.git
   
   # Fetch and merge changes from upstream
   git fetch upstream
   git checkout main
   git merge upstream/main
   git push origin main
   ```

---

## 💬 Commit Message Style

We follow the **Conventional Commits** specification for clear and consistent commit messages.

### Format

```
<type>(<scope>): <subject>

<body> (optional)

<footer> (optional)
```

### Types

- **feat**: A new feature
  - Example: `feat(frontend): add certificate preview component`
  
- **fix**: A bug fix
  - Example: `fix(backend): resolve certificate generation error`
  
- **docs**: Documentation changes
  - Example: `docs(readme): update installation instructions`
  
- **style**: Code style changes (formatting, missing semicolons, etc.)
  - Example: `style(frontend): format code with prettier`
  
- **refactor**: Code refactoring without changing functionality
  - Example: `refactor(backend): simplify certificate service logic`
  
- **test**: Adding or updating tests
  - Example: `test(api): add unit tests for certificate endpoint`
  
- **chore**: Maintenance tasks, dependency updates
  - Example: `chore(deps): update react to v18.2.0`
  
- **perf**: Performance improvements
  - Example: `perf(backend): optimize image processing`

### Examples

**Good commit messages:**
```bash
feat(frontend): add certificate download button
fix(backend): correct PDF generation filename format
docs(contributing): add branch naming conventions
refactor(api): improve error handling in certificate route
chore(deps): update fastapi to v0.104.0
```

**Bad commit messages:**
```bash
update stuff
fixed bug
changes
asdf
Update README.md
```

### Guidelines

- Use the imperative mood ("add" not "added" or "adds")
- Keep the subject line under 50 characters
- Capitalize the first letter of the subject
- Don't end the subject line with a period
- Use the body to explain **what** and **why**, not **how**

---

## ✅ Contribution Guidelines

* Only **quality PRs** will be merged (no spam).
* Each PR should focus on **a single change/feature**.
* Add proper documentation/comments where necessary.
* Be respectful and constructive in reviews/discussions.

---

## 🏷️ What You Can Contribute

* Fixing typos, grammar, or documentation improvements.
* Adding beginner-friendly code snippets.
* Enhancing project structure.
* Suggesting and implementing new beginner-friendly challenges.

---

## 📜 Code of Conduct

We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
By participating, you agree to uphold a welcoming and inclusive environment.
