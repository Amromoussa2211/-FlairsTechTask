# orangehrm-cypress-project/orangehrm-cypress-project/README.md

# OrangeHRM Cypress Project

This project is an automated testing suite for the OrangeHRM website using Cypress. It follows best practices and utilizes the Page Object Model (POM) design pattern to ensure maintainability and scalability of the test code.

## Project Structure

The project is organized as follows:

```
orangehrm-cypress-project
├── cypress
│   ├── e2e
│   │   ├── tests
│   │   │   ├── login.spec.js        # Test cases for login functionality
│   │   │   └── dashboard.spec.js     # Test cases for dashboard functionality
│   │   ├── pages
│   │   │   ├── loginPage.js          # Page object for login page
│   │   │   └── dashboardPage.js       # Page object for dashboard
│   ├── fixtures
│   │   └── example.json              # Example data for tests
│   ├── plugins
│   │   └── index.js                   # Plugin configuration
│   ├── support
│   │   ├── commands.js                # Custom commands for Cypress
│   │   └── e2e.js                     # Global configurations for tests
├── cypress.config.js                  # Cypress configuration file
├── package.json                       # npm configuration file
└── README.md                          # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/orangehrm-cypress-project.git
   cd orangehrm-cypress-project
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the tests:**
   ```
   npx cypress open
   ```
   This will open the Cypress Test Runner where you can select and run the tests.

## Usage

- The tests are organized into two main categories: login and dashboard.
- Each test file utilizes the Page Object Model to interact with the application, making the tests more readable and maintainable.

## Bonus Tasks

- Implemented additional test cases for edge scenarios in both login and dashboard functionalities.
- Added custom commands to enhance test capabilities.

## Contributing

Feel free to submit issues or pull requests to improve the project. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.