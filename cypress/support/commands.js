// This file defines custom commands for Cypress to enhance testing capabilities. 

Cypress.Commands.add('login', (username, password) => {
  cy.visit('/web/index.php/auth/login'); // Visit the login page URL
  cy.get('input[name="username"]').type(username);
  cy.get('input[name="password"]').type(password);
  cy.get('button[type="submit"]').click();
  // Verify successful login by checking the URL or a specific element
  cy.url().should('include', '/dashboard');
  cy.get('.welcome').should('contain', 'Welcome');
});

Cypress.Commands.add('addUser', (userData) => {
  cy.get('button#addUser').click();
  cy.get('input[name="username"]').type(userData.username);
  cy.get('input[name="password"]').type(userData.password);
  cy.get('input[name="confirmPassword"]').type(userData.password);
  cy.get('button[type="submit"]').click();
});

Cypress.Commands.add('deleteUser', (username) => {
  cy.get('table').contains(username).parents('tr').find('button.delete').click();
  cy.get('button.confirm').click();
});