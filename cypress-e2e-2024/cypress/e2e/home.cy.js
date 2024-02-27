describe('Homepage', () => {

  beforeEach(() => {
    cy.visit('/')
  })

  it('is accessible', () => {
    cy.get('h1').contains('Kitchen Sink')
    cy.get('.banner .container p').contains('example app used to showcase')
  })

  it('has full content', () => {
    cy.get('h1').scrollIntoView({ offset: { top: 600, left: 0} })
    cy.wait(2000)
  })

  it('has main nav', () => {
    cy.get('a[href="/utilities"]').first().click()
    cy.url().should('include', '/utilities')
    cy.get('h1').contains('Utilities')
    cy.get('.banner .container p').contains('use of methods from other commonly used libraries ')

    cy.visit('/')
    cy.get('a[href="/cypress-api"]').first().click()
    cy.url().should('include', 'cypress-api')
    cy.get('h1').contains('Cypress API')
    cy.get('.banner .container p').contains('uses of the Cypress API')
  })
})