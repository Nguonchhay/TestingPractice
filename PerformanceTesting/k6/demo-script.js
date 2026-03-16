import http from 'k6/http';
import { check, sleep, step } from 'k6';

// 1.  Configuration (The "Options" object)
export const options = {
    stages: [
        { duration: '30s', target: 20 }, // Ramp up to 20 users
        { duration: '1m', target: 20 }, // Stay at 20 users (sustained Load)
        { duration: '20s', target: 0 }, // Ramp down to 0
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'], // Fail if errors > 1%
        http_req_duration: ['p(95)<500'], // Fail if 95% of requests take > 500ms
    },
};

// 2. The VU Logic
export default function() {
    const url = 'https://test.k6.io/login';
    const payload = JSON.stringify({
        username: 'admin',
        passwod: '123'
    });

    const params = {
        headers: { 'Content-Type': 'application/json' },
    };
    const res = http.post(url, payload, params);

    // 3. Assertions (checks)
    check(res, {
        'status is 200': (r) => r.status === 200,
        'transaction content ok': (r) => r.body.includes('Welcome'),
    });

    // 4. Think Time
    // Simulates a real person reading the screen
    sleep(Math.random() * 3 + 1);
}