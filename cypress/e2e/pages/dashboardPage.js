class DashboardPage {
  get adminTab() {
    return cy.get('a.oxd-main-menu-item[href="/web/index.php/admin/viewAdminModule"]');
  }

  get recordCount() {
    return cy.get('.oxd-text.oxd-text--span');
  }

  // get addButton() {
  //   return cy.get('button.oxd-button--secondary');
  // }

  // get usernameInput() {
  //   return cy.get('input[name="username"]');
  // }

  // get passwordInput() {
  //   return cy.get('input[name="password"]');
  // }

  // get saveButton() {
  //   return cy.get('#btnSave');
  // }

  get searchInput() {
    return cy.get('#searchSystemUser_userName');
  }

  get deleteButton() {
    return cy.get('#btnDelete');
  }

  clickAdminTab() {
    this.adminTab.click();
  }

  getRecordCount() {
    return this.recordCount.invoke('text');
  }

  clickAddButton() {
    this.addButton.click();
  }

  fillRequiredData(username, password) {
    this.usernameInput.type(username);
    this.passwordInput.type(password);
  }

  clickSaveButton() {
    this.saveButton.click();
  }

  searchUser(username) {
    this.searchInput.type(username);
  }

  deleteUser() {
    this.deleteButton.click();
  }
}

export default DashboardPage;