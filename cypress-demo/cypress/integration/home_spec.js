describe('Homepage Test', () => {
    it('has logo', () => {
        cy.visit('/')
        cy.url().should('include', '/')
        cy.get('#nav-logo').should('exist')
    })
})