describe('Order Tourist SIM', () => {
    Cypress._.times(1, (num) => {
        it(`Order SIM for ${num + 1} times`, () => {
            cy.visit('/simsales/1001')

            // Step 1: order detail
            cy.contains('Pick up location').scrollIntoView()

            cy.wait(1000)
            cy.contains('Phnom Penh International Airport').click()

            cy.get('.expected-date > button').click()
            cy.wait(500)
            cy.get('button[name="day"]').last().click()
            cy.wait(500)
            cy.get('body').click()
            cy.wait(500)
            cy.get('button[type="submit"]').click()

            // Step 2: Upload information
            cy.wait(500)
            const email = `test.${Date.now()}@gmail.com`
            cy.get('input[name="Email"]').type(email)
            cy.get('input[name="Confirm Email"]').type(email)

            cy.get('input[type=file]').attachFile('cambodia-id-card.jpg')

            cy.contains('I have read and agree to the website').click()
            cy.contains('Please confirm your uploaded document is valid').click()
            cy.get('button[type="submit"]').click()

            // Step 3: Make payment
            cy.wait(3000)
            cy.contains('Choose Payment Method').should('be.visible')
            cy.get('button[type="submit"]').click()
            cy.wait(5000)

            // Close payment popup
            cy.get('.aba-close-button').click()
            cy.on('window:confirm',() => true)
            cy.wait(5000)
            cy.contains('Selected SIM package').should('be.visible')
        })
    })
})