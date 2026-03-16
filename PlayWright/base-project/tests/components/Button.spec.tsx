import { test, expect } from '@playwright/experimental-ct-react';
import Button from '@/src/components/Button';

test('Button triggers click event', async ({ mount }) => {
  let clicked = false;
  const component = await mount(
    <Button label="Click Me" onClick={() => (clicked = true)} />
  );
  
  await component.click();
  expect(clicked).toBe(true);
});