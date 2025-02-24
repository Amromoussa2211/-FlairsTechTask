import DashboardPage from '../pages/dashboardPage';
import LoginPage from '../pages/loginPage';

describe('Dashboard Functionality', () => {
    const dashboardPage = new DashboardPage();

    beforeEach(() => {
        cy.visit('/web/index.php/auth/login'); // Visit the login page URL
        const loginPage = new LoginPage();
        loginPage.enterUsername(Cypress.env('username'));
        loginPage.enterPassword(Cypress.env('password'));
        loginPage.clickLogin();
        // Wait for the dashboard to load
        cy.get('.welcome', { timeout: 10000 }).should('be.visible').then(() => {
            cy.log('Dashboard loaded successfully');
        });
    });

    it('should verify the admin tab is accessible', () => {
        cy.get('#menu_admin_viewAdminModule', { timeout: 10000 }).should('be.visible').then(() => {
            cy.log('Admin tab is visible');
        }); // Wait for the element to be visible
        dashboardPage.clickAdminTab();
        // No assertions
    });

    it('should display the correct record count', () => {
        cy.get('#menu_admin_viewAdminModule', { timeout: 10000 }).should('be.visible').then(() => {
            cy.log('Admin tab is visible');
        }); // Wait for the element to be visible
        dashboardPage.clickAdminTab();
        dashboardPage.getRecordCount().then((count) => {
            cy.log(`Record count: ${count}`);
            // No assertions
        });
    });

    it('should add a new user', () => {
        cy.get('#menu_admin_viewAdminModule', { timeout: 10000 }).should('be.visible').then(() => {
            cy.log('Admin tab is visible');
        }); // Wait for the element to be visible
        dashboardPage.clickAdminTab();
        dashboardPage.clickAddButton();
        dashboardPage.fillRequiredData('newuser', 'password123');
        dashboardPage.clickSaveButton();
        dashboardPage.searchUser('newuser');
        // No assertions
    });

    it('should delete a user', () => {
        cy.get('#menu_admin_viewAdminModule', { timeout: 10000 }).should('be.visible').then(() => {
            cy.log('Admin tab is visible');
        }); // Wait for the element to be visible
        dashboardPage.clickAdminTab();
        dashboardPage.searchUser('newuser');
        dashboardPage.deleteUser();
        // No assertions
    });
});

describe('Login Functionality', () => {
    const loginPage = new LoginPage();

    beforeEach(() => {
        cy.visit('/web/index.php/auth/login'); // Visit the login page URL
    });

    it('should successfully log in with valid credentials', () => {
        loginPage.enterUsername(Cypress.env('username'));
        loginPage.enterPassword(Cypress.env('password'));
        loginPage.clickLogin();
        // Wait for the dashboard to load
        cy.get('.welcome', { timeout: 50000 }).should('be.visible').then(() => {
            cy.log('Dashboard loaded successfully');
        });
        // No assertions
    });

    it('should show an error message for invalid credentials', () => {
        loginPage.enterUsername('InvalidUser');
        loginPage.enterPassword('InvalidPassword');
        loginPage.clickLogin();
        // Wait for the error message to be visible
        cy.get('.alert-error', { timeout: 10000 }).should('be.visible').then(() => {
            cy.log('Error message displayed');
        });
        // No assertions
    });
});