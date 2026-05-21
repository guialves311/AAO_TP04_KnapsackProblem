### Project Setup

The project was made with the .venv environment for Python to allow for reproductibility of it's functionalities. Upon repository cloning, after opening it on a code editor of your choice, run this command on terminal:

- `python -m venv .venv`: Command that creates the environment on your local PC.

After setting up the environment, you'll need to activate it, with the following command:

- `.\.venv\Scripts\Activate.ps1`: On PowerShell terminal (Windows)
- `.\.venv\Scripts\activate.bat`: On CMD terminal (Windows) - Be careful to have the correct folder open on terminal before running command
- `source .venv/bin/activate`: On bash / zsh terminal (Linux / macOS)
* Incase your OS don't allow it to activate, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` (Windows only)

To help with code setup and running, if you don't have any Python extensions installed, here's a list of the extensions installed that were utilized for this project: (Name - Owner)

- `Python Extension Pack - Don Jayamanne`: This extension installs a number of extensions alongside it, all used in this project
- `Python Debugger - Microsoft`
- `Python Environments - Microsoft`
- `Pylance - Microsoft`

Inside the repository, there's a file called requirements.txt, which is where Python stores all libraries installed and it's versions, allowing for easy library implementation. To implement those libraries onto your environment, run this command on your terminal:

- `pip install -r requirements.txt`: Recreates the environment libraries

Incase you want to leave the .venv environment, simply run `deactivate` on your terminal. The instruction to activate it was mentioned beforehand.

To run the main file, run this command:

- `python main.py`: Runs the main file


### Environment Variables

The project uses the following environment variables defined in the `.env` file:

- `DATA_FILE = 'src\\data\\instances'`: Path to the data file containing the problem instances.
- `NUM_ITERATIONS = 1000`: Number of iterations for the algorithm.
- `TEMPERATURE = 10000000000`: Initial temperature for simulated annealing.
- `COOLING_RATE = 0.999`: Cooling rate for simulated annealing.

