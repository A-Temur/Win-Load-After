# Win Load After

**Win Load After** is a small Python utility for Windows that creates a scheduled task to ensure one program (e.g., Razer Synapse) only starts *after* another specified program (e.g., motherboard software) has launched and a user-defined delay has passed.

## 📦 Features

* Create a Windows Task Scheduler job that:

  * Monitors for a specific process to be running.
  * Launches a second executable after a given delay.
  * Executes on every user login.
* Useful for dependency-aware auto-start of software.

## ⚙️ How It Works

1. The user specifies:

   * **Load-before process name** (e.g., `AsusMotherboard.exe` or `ArmouryCrate`.)
   * **Executable to launch after** (e.g., `RazerSynapse.exe`)
   * **Startup delay in seconds**
2. The script:

   * Creates a Python script that performs the check and delay logic.
   * Registers a Windows Task Scheduler task to run this script in the background on user login.

## 🚀 Example Use Case

> Ensure Razer Synapse only starts *after* ASUS motherboard tools are fully running:
>
> 1. Type in the process to wait for: `ArmouryCrate`
> 2. Select the Executable to start via GUI.
> 3. Type in a delay in seconds.

## 🛠 Requirements

* Python 3.11
* Windows 11
* Admin rights (for task scheduler)
* easygui~=0.98.3
* pyuac~=0.0.3
* psutil~=5.9.8

## 📥 Auto Installation 

1. Clone or download this repo:

   ```bash
   git clone https://github.com/A-Temur/win-load-after.git
   ```

2. Click on install.vbs:

   * this will automatically install the python dependencies and will run the program after that.

## 📥 Manual Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/A-Temur/win-load-after.git
   cd win-load-after
   ```

2. Install required Python packages (if any):

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

Just double-click on start.vbs, a simple GUI will appear.


## 📝 Notes

* The monitoring script runs silently in the background.
* The Windows task is persistent and re-runs at every user login.
* To remove the task, use the Task Scheduler GUI or `schtasks /delete`.