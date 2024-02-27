describe('Form elements', () => {
    beforeEach(() => {
        cy.visit('/commands/actions')
    })

    it('page is accessible', () => {
        cy.get('h1').contains('Actions')
        cy.get('.banner .container p').contains('actions being performed on DOM elements in Cypress')
    })
})