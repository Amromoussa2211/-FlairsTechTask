module.exports = {
  e2e: {
    setupNodeEvents(on, config) {
      return require('./cypress/plugins/index.js')(on, config);
    },
    baseUrl: "https://opensource-demo.orangehrmlive.com", // Base URL of the OrangeHRM site
    supportFile: 'cypress/support/e2e.js',
    specPattern: 'cypress/e2e/tests/**/*.spec.js',
    experimentalStudio: true,
    screenshotsFolder: 'cypress/screenshots',
    videosFolder: 'cypress/videos',
    screenshotOnRunFailure: true,
    env: {
      username: 'Admin', // Set your username here
      password: 'admin123' // Set your password here
    }
  },
};