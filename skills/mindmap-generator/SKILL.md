# 思维导图生成技能 (Mind Map Generator)

## 触发场景
用户要求将文档（如测试需求分析报告、PRD 等）转换为**思维导图**，或说"生成思维导图"、"输出为 HTML 思维导图"。

## 核心原则

### ⚠️ 必须使用 `<details>/<summary>` 原生标签
- **不要用 JS onclick 事件来做折叠/展开** — 这是导致多次返工的根本原因
- 浏览器原生支持，100% 可靠，无需任何 JS 就能工作
- 展开：`details[open]` 或 JS 设置 `detailsEl.open = true`
- 折叠：JS 设置 `detailsEl.open = false`

### ✅ 标准结构
```html
<details open>                          <!-- open = 默认展开，可选 -->
  <summary>
    <span class="toggle"></span>       <!-- + / − 图标，由 CSS 控制 -->
    <span class="node-label">节点标题</span>
    <span class="count-tag">(12个)</span>
    <span class="p0-badge">P0×3</span>  <!-- 可选 -->
  </summary>
  <div class="children">               <!-- 或 leaf-children -->
    <!-- 子节点 -->
  </div>
</details>
```

### ✅ 标准 CSS
```css
details { margin-left: 0; }
summary { 
    list-style: none; cursor: pointer; user-select: none;
    display: flex; align-items: center; padding: 5px 0;
}
summary::-webkit-details-marker { display: none; }  /* 隐藏默认三角 */
/* 手动 + / − 图标 */
summary .toggle {
    display: inline-flex; align-items: center; justify-content: center;
    width: 18px; height: 18px; border-radius: 3px;
    background: #2a2a4a; margin-right: 6px; font-size: 11px;
    border: 1px solid #444; color: #aaa;
}
details[open] > summary > .toggle {   /* 展开时图标变红 */
    background: #e94560; border-color: #e94560; color: #fff;
}
/* 子容器缩进 */
.children, .leaf-children { padding-left: 30px; }
/* 叶节点样式 */
.leaf { padding-left: 20px; position: relative; }
.leaf::before { /* 连接线 */ }
```

### ✅ "全部展开/折叠" 按钮
仅需极简 JS，控制在 `details` 元素上：
```javascript
function expandAll() {
    document.querySelectorAll('details').forEach(function(d) { d.open = true; });
}
function collapseAll() {
    document.querySelectorAll('details').forEach(function(d) { d.open = false; });
}
```

### ❌ 禁止使用
- `onclick="..."` 处理折叠
- `classList.add/remove('open')` + CSS `display: none/block`
- 任何需要 JS 才能实现折叠的方案
- `Element.classList` 判断状态（浏览器兼容性差）

## 输出要求
- 单文件 HTML，零外部依赖
- 响应式深色主题，适合演示
- 优先级用颜色区分：P0=红色，P1=橙色，P2=蓝色
- 统计卡片显示总数
- 树形层级清晰，缩进一致

## 常见优先级
- 用户要求生成思维导图时，优先使用此技能
- 如果用户明确要求其他格式（Mermaid、markmap 等），按用户要求执行
