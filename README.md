# PyNextjs 🚀

Welcome to **PyNextjs** – an advanced Python tool for creating and configuring a Next.js application effortlessly! This tool integrates several key setup steps and optional features, giving you a customizable development environment right from the start. It features a stylish interface powered by the `rich` and `pyfiglet` libraries to make project creation an enjoyable experience.

## Features 🎉

With **PyNextjs**, you can:
- 🏗️ **Create a new Next.js app** (in JavaScript or TypeScript)
- 🎨 **Add Tailwind CSS** for styling
- 📁 **Generate initial pages and components** to get started
- 🔒 **Set up environment variables** with a `.env` file
- 🌍 **Initialize a Git repository** for version control
- 🐳 **Set up Docker configuration** for containerized deployment
- 📦 **Install additional packages** like ESLint, Prettier, and Axios
- 🌈 **Enjoy a beautiful, rich interface** thanks to `rich` and `pyfiglet`

## Requirements 📋

- Python 3.6 or higher
- Node.js and npm installed
- Internet connection to install dependencies

> **Note**: Make sure to install the required Python libraries for `rich` and `pyfiglet`:
> ```bash
> pip install rich pyfiglet
> ```

## Installation & Usage ⚙️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/PyNextjs.git
   cd PyNextjs
   ```

2. **Run the script**:
   ```bash
   python pynext.py
   ```

3. Follow the on-screen prompts to customize your Next.js project setup.

## Step-by-Step Guide 🧑‍🏫

### 1. Project Name 📝
You’ll first be prompted to enter a **project name** for your Next.js app. This name will be used to create the project directory.

### 2. Choose TypeScript Option 📐
You can choose whether to use **TypeScript** (recommended for strongly-typed JavaScript). Simply type `y` for TypeScript or `n` to use JavaScript.

### 3. Install Tailwind CSS (Optional) 🎨
**Tailwind CSS** is an optional addition to style your project. If you choose to install it, Tailwind configuration files will be generated automatically.

### 4. Create Initial Pages and Components 📂
The tool can create a basic `index` page and an example component, which is especially useful for beginners looking to understand Next.js structure.

### 5. Set Up Environment Variables 🔐
An optional **`.env` file** will be created to manage environment variables. This is helpful for setting up API URLs or sensitive information like API keys.

### 6. Initialize Git Repository (Optional) 🌐
If you choose this option, a **Git repository** will be initialized in the project folder, enabling version control from the start.

### 7. Set Up Docker Files 🐳
Opt to set up Docker configuration files, including:
   - A **Dockerfile** for building and running your app in a containerized environment.
   - A **docker-compose.yml** file for easy multi-service setup.

This option is helpful if you plan to deploy your Next.js app with Docker.

### 8. Install Additional Packages 📦
Choose to install:
   - **ESLint**: Ensures code consistency.
   - **Prettier**: Auto-formats code for readability.
   - **Axios**: Helps with HTTP requests.

## Files Generated 📁

Based on your selections, **PyNextjs** generates the following files:
- `package.json`: Standard Next.js file with selected dependencies
- `tailwind.config.js` (if Tailwind CSS is installed)
- `Dockerfile` and `docker-compose.yml` (if Docker is selected)
- `.env.local`: Environment file with sample variables
- Basic pages (`index.js/tsx`) and components (`ExampleComponent.js/tsx`)

## Example Usage 🚀

To start your Next.js app, navigate to the project folder and run:

```bash
cd project-name
npm run dev
```

Then, open [http://localhost:3000](http://localhost:3000) in your browser to see your new app in action!

## Contributing 🤝

Contributions are welcome! Feel free to submit a pull request or open an issue with your ideas for new features or improvements.

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

With **PyNextjs**, setting up a Next.js project is quick, customizable, and visually engaging. We hope you enjoy using it to streamline your development workflow! 🥳
