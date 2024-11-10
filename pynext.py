import os
import subprocess
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import pyfiglet

# Initialize the rich console
console = Console()

def create_nextjs_app():
    # Display ASCII banner using pyfiglet
    banner = pyfiglet.figlet_format("PyNextjs")
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print(Text("Welcome to the PyNextjs App Generator by RK!", style="bold magenta"))

    # Prompt for the project name
    project_name = Prompt.ask("Enter the project name for your Next.js app: ")

    # Check if project directory already exists
    if os.path.exists(project_name):
        console.print(f"[bold red]The directory '{project_name}' already exists. Please choose a different name.[/bold red]")
        return

    # Choose JavaScript or TypeScript
    language_choice = Prompt.ask("Do you want to use TypeScript? ", choices=["y", "n"], default="n")
    use_typescript = language_choice == 'y'

    # Command to create a Next.js app
    cmd = ["npx", "create-next-app", project_name]
    if use_typescript:
        cmd.append("--ts")

    # Run the command to create the app
    try:
        console.print(f"[bold green]Creating Next.js app '{project_name}' with TypeScript: {use_typescript}[/bold green]")
        subprocess.run(cmd, check=True)
        console.print(f"[bold green]Next.js app '{project_name}' created successfully![/bold green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error creating Next.js app: {e}[/bold red]")
        return

    # Change directory to the project
    os.chdir(project_name)

    # Install Tailwind CSS (optional)
    install_tailwind = Prompt.ask("Do you want to install Tailwind CSS? ", choices=["y", "n"], default="n")
    if install_tailwind == 'y':
        try:
            console.print("[bold cyan]Installing Tailwind CSS...[/bold cyan]")
            subprocess.run(["npx", "tailwindcss", "init", "-p"], check=True)
            with open("tailwind.config.js", "w") as f:
                f.write("module.exports = { purge: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'], darkMode: false, theme: { extend: {}, }, variants: { extend: {}, }, plugins: [], };")
            console.print("[bold cyan]Tailwind CSS installed and configured.[/bold cyan]")
        except subprocess.CalledProcessError:
            console.print("[bold red]Failed to install Tailwind CSS.[/bold red]")

    # Generate initial pages and components
    create_initial_structure = Prompt.ask("Do you want to create initial pages and components?", choices=["y", "n"], default="y")
    if create_initial_structure == 'y':
        os.makedirs("pages/api", exist_ok=True)
        os.makedirs("components", exist_ok=True)
        
        # Create example page
        page_file = "pages/index.js" if not use_typescript else "pages/index.tsx"
        with open(page_file, "w") as f:
            f.write("import Head from 'next/head';\n\nexport default function Home() {\n  return (\n    <div>\n      <Head>\n        <title>Home</title>\n      </Head>\n      <main>\n        <h1>Welcome to Next.js!</h1>\n      </main>\n    </div>\n  );\n}")

        # Create example component
        component_file = "components/ExampleComponent.js" if not use_typescript else "components/ExampleComponent.tsx"
        with open(component_file, "w") as f:
            f.write("export default function ExampleComponent() {\n  return (\n    <div>\n      <p>This is an example component.</p>\n    </div>\n  );\n}")
        console.print("[bold green]Initial pages and components created.[/bold green]")

    # Set up .env file
    setup_env = Prompt.ask("Do you want to set up a .env file for environment variables? ", choices=["y", "n"], default="y")
    if setup_env == 'y':
        with open(".env.local", "w") as f:
            f.write("NEXT_PUBLIC_API_URL=http://localhost:3000/api\n")
        console.print("[bold green]Environment file (.env.local) created with sample variables.[/bold green]")

    # Initialize Git repository (optional)
    git_init = Prompt.ask("Do you want to initialize a Git repository? ", choices=["y", "n"], default="y")
    if git_init == 'y':
        subprocess.run(["git", "init"], check=True)
        console.print("[bold green]Git repository initialized.[/bold green]")

    # Set up Docker files (optional)
    setup_docker = Prompt.ask("Do you want to set up Docker files? ", choices=["y", "n"], default="n")
    if setup_docker == 'y':
        dockerfile_content = (
            "FROM node:14-alpine\n"
            "WORKDIR /app\n"
            "COPY package.json .\n"
            "RUN npm install\n"
            "COPY . .\n"
            "EXPOSE 3000\n"
            "CMD [\"npm\", \"run\", \"dev\"]"
        )
        docker_compose_content = (
            "version: '3'\n"
            "services:\n"
            "  web:\n"
            "    build: .\n"
            "    ports:\n"
            "      - '3000:3000'\n"
        )
        with open("Dockerfile", "w") as f:
            f.write(dockerfile_content)
        with open("docker-compose.yml", "w") as f:
            f.write(docker_compose_content)
        console.print("[bold green]Docker and Docker Compose files created.[/bold green]")

    # Install additional packages
    additional_packages = Prompt.ask("Install additional packages (ESLint, Prettier, Axios)? ", choices=["y", "n"], default="y")
    if additional_packages == 'y':
        subprocess.run(["npm", "install", "--save-dev", "eslint", "prettier"], check=True)
        subprocess.run(["npm", "install", "axios"], check=True)
        console.print("[bold cyan]ESLint, Prettier, and Axios installed.[/bold cyan]")

    console.print("[bold magenta]Setup complete! Your Next.js app is ready with advanced configurations.[/bold magenta]")

# Run the tool
create_nextjs_app()
      
