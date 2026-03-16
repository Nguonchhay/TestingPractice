import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://github.com/login');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Sign in to GitHub/);
});
