import { test, expect } from '@playwright/test';

test('Should get users via API', async ({ request }) => {
  const response = await request.get('/users');
  expect(response.ok()).toBeTruthy();
  expect(response.status()).toBe(200);
  
  const body = await response.json();
  // Verify the entire array structure
  expect(body).toEqual(expect.arrayContaining([
    expect.objectContaining({
      id: expect.any(Number),
      name: expect.any(String),
    })
  ]));
});
