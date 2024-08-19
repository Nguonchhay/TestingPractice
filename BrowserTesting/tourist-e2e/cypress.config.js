const { defineConfig } = require("cypress");

module.exports = defineConfig({
  reporter: 'mochawesome',
  reporterOptions: {
    reportDir: 'cypress/reports/results',
    overwrite: false,
    html: true,
    json: true,
  },
  video: true,
  videoCompression: true,
  videosFolder: 'cypress/videos_record',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    projectId: 'TouristPlus_E2E',
    baseUrl: 'https://qa-store.cellcard.com.kh',
  },
});
