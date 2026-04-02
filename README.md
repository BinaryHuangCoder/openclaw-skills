# OpenClaw 公共技能仓库

这是 OpenClaw 的公共技能仓库，提供各种开箱即用的技能扩展。

## 安装使用
用户只需要对自己的 OpenClaw 说：`安装【技能名称】技能`，即可自动从本仓库下载安装使用，无需任何手动配置。

## 现有技能列表
| 技能 ID | 技能名称 | 版本 | 描述 |
| --- | --- | --- | --- |
| requirement-to-uat-cases | 需求转 UAT 测试案例工具 | v1.1.0 | 读取 Word 格式的银行业务需求文档，自动生成符合银行规范的用户验收测试（UAT）案例，支持批量处理，减少业务人员手动编写工作量 |
| test-requirement-analyzer | 测试需求分析专家 | v1.0.0 | 系统化分析需求文档并识别测试验证点，生成结构化的测试分析输出，支持多种文档格式，可输出 HTML 格式的完整测试报告（多表格分 Sheet） |
| test-case-designer | 测试案例设计专家 | v1.0.0 | 将测试需求分析结果转换为企业标准格式的结构化、可执行测试案例文档，支持多种输出格式（Excel/HTML/CSV/Markdown），按优先级分级，多测试类型覆盖 |

## 目录结构
```
openclaw-skills/
├── README.md # 项目总说明
├── manifest.json # 技能清单索引（核心文件，自动生成）
├── .gitignore
└── skills/ # 所有技能存放目录，按功能领域分类
    ├── business-testing/ # 业务测试领域技能
    │   └── requirement-to-uat-cases/ # 需求转 UAT 测试案例技能
    │       ├── skill.json # 技能元数据
    │       ├── src/ # 源代码
    │       ├── config/ # 配置文件示例
    │       ├── docs/ # 技能专用文档
    │       └── tests/ # 单元测试
    ├── test-requirement-analyzer/ # 测试需求分析技能
    │   ├── SKILL.md # 技能说明文档
    │   └── scripts/ # 脚本文件
    │       └── gen_report.py # 报告生成脚本
    ├── test-case-designer/ # 测试案例设计技能
    │   ├── SKILL.md # 技能说明文档
    │   ├── README.md # 技能说明
    │   └── 测试案例企业标准模版.xlsx # 企业标准模板
    ├── data-processing/ # 数据处理领域技能
    ├── api-integration/ # API 集成领域技能
    └── ... # 其他领域技能
```

## 技能开发指南

### 创建新技能
1. 在 `skills/` 目录下创建技能文件夹
2. 编写 `SKILL.md` 文件（必需）
3. 添加脚本文件（可选）
4. 更新 `manifest.json`
5. 更新 `README.md`

### SKILL.md 规范
- 包含技能描述和触发场景
- 定义输入输出格式
- 提供使用示例
- 说明依赖和配置

## 贡献指南
欢迎提交新的测试相关技能！
