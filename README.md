# Load After

## Overview
Startup Load Order Customizer is a Windows application designed to manage and customize the order in which executables load upon system startup. 
This tool is especially useful for ensuring that sensitive software, such as Razer Synapse, loads in an environment optimized for its operation—potentially after other critical services like motherboard software have initialized.
Besides that this tool will provide you an automatic way of blocking internet access for a third party software and all oft its processes and services.

## Features
- **Customizable Load Order:** Set the exact order you want your applications to start when Windows boots up.
- **Delayed Start:** Introduce a delay between the start of applications to avoid conflicts.
- **Block Internet Access:** Set up auto blocking of internet access for the third party Software and all related processes/services.
- **Change the services startups:** Set up how the related services will start (Auto, autodelay, manual, disable)
- **User-Friendly Interface:** Easily configure your startup settings with a simple and intuitive interface.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Windows 10 or newer

### Installing
1. Download the latest release from the GitHub releases page.
2. Run the installer and follow the on-screen instructions.

## Usage
To use Startup Load Order Customizer, follow these steps:

1. Open the application.
2. Add applications to the list using the 'Add' button.
3. Use the up and down arrows to adjust the order of the applications.
4. Set a delay for each application if needed.
5. Save the configuration.
6. Enable the custom load order by toggling the 'Enable' switch.

## Built With
- [Python](https://www.python.org/) - The programming language used.
- [PyQt](https://riverbankcomputing.com/software/pyqt/intro) - Used to create the graphical user interface.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/startup-load-order-customizer/tags).

## Authors
- **Your Name** - *Initial work* - [YourUsername](https://github.com/YourUsername)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Hat tip to anyone whose code was used.
- Special thanks to community contributions.
- Inspiration: Challenges with Razer Synapse's sensitivity to load order.

