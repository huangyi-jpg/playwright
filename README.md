# Playwright 演示项目

## 先决条件
- Node.js 18+
- Playwright 1.42+

## 安装
```bash
npm install
```

## 运行测试
```bash
npm test
```

## 功能
- 端到端测试
- 视觉对比
- CI集成

## 示例代码
```js
const { test, expect } = require('@playwright/test');

test('基本示例', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveTitle('Example Domain');
});
```